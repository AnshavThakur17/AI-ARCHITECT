from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.request_model import PromptRequest

from app.services.llm_extractor import extract_with_llm
from app.services.decision_engine import system_decisions
from app.services.recommendation_engine import recommend_architecture
from app.services.database_recommender import recommend_database
from app.services.cache_recommender import recommend_cache
from app.services.failure_predictor import predict_failures
from app.services.reasoning_engine import generate_reasoning
from app.services.diagram_generator import generate_diagram

from app.services.persistence import save_analysis
from app.services.requirement_extractor import extract_requirements
from app.services.cost_estimator import estimate_cost
import re


router = APIRouter()


@router.post("/analyze")
def analyze(
    data: PromptRequest,
    db: Session = Depends(get_db)
):

    # AI extraction
    requirements = extract_with_llm(
        data.prompt
    )

    # safety defaults
    requirements.setdefault("real_time", False)
    requirements.setdefault("low_latency", False)
    requirements.setdefault("write_heavy", False)
    requirements.setdefault("read_heavy", False)
    requirements.setdefault("security_critical", False)
    requirements.setdefault("geo_distributed", False)
    requirements.setdefault("consistency_requirement", "normal")
    requirements.setdefault("scale", 10000)

    # Sanitize scale value to be an integer
    try:
        if isinstance(requirements.get("scale"), str):
            requirements["scale"] = int(requirements["scale"].replace(",", "").strip())
        else:
            requirements["scale"] = int(requirements["scale"])
    except (ValueError, TypeError):
        if isinstance(requirements.get("scale"), str):
            val_str = requirements["scale"].replace(",", "")
            match = re.search(r'(\d+)', val_str)
            if match:
                val = int(match.group(1))
                if "million" in requirements["scale"].lower():
                    requirements["scale"] = val * 1000000
                elif "k" in requirements["scale"].lower() or "thousand" in requirements["scale"].lower():
                    requirements["scale"] = val * 1000
                else:
                    requirements["scale"] = val
            else:
                requirements["scale"] = 10000
        else:
            requirements["scale"] = 10000

    decisions = system_decisions(
        requirements
    )

    architecture = recommend_architecture(
        requirements
    )

    database = recommend_database(
        requirements
    )

    cache = recommend_cache(
        decisions
    )

    failures = predict_failures(
        requirements,
        decisions
    )

    reasoning = generate_reasoning(
        requirements,
        decisions,
        architecture
    )

    diagram = generate_diagram(
        architecture,
        database["database"]
    )

    # Save to history database
    try:
        extra_info = extract_requirements(data.prompt)
        app_type = extra_info.get("app_type", "unknown")
        cost_info = estimate_cost(
            scale=requirements["scale"],
            database=database.get("database"),
            cache=cache.get("cache"),
            needs_queue=decisions.get("needs_queue", False),
            needs_cdn=decisions.get("needs_cdn", False)
        )
        cost = cost_info.get("monthly_cost_usd", 250)

        save_analysis(
            db=db,
            prompt=data.prompt,
            app_type=app_type,
            architecture=architecture,
            database=database["database"],
            cost=cost,
            scale=requirements["scale"]
        )
    except Exception as db_err:
        # Log error or print, but don't fail the request if database save fails
        print(f"Error saving analysis to database: {db_err}")
        # Make sure cost_info has a fallback structure
        cost_info = {
            "servers_needed": 1,
            "monthly_cost_usd": 250
        }

    return {

        "llm_understanding": requirements,

        "system_decisions": decisions,

        "architecture": architecture,

        "architecture_reasoning": reasoning,

        "architecture_diagram": diagram,

        "database_choice": database,

        "cache_layer": cache,

        "predicted_failures": failures,

        "cost_estimate": cost_info
    }