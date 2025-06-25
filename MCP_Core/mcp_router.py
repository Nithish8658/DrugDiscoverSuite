# mcp_router.py

from Agents.TargetIdentifier import target_generator
from Agents.CompoundGenerator import compound_generator

def run_pipeline(disease: str):
    """
    Orchestrates the full pipeline: identifies the biological target,
    then generates compounds based on that target.
    """
    # Step 1: Identify the biological target
    target_result = target_generator.identify_target(disease)
    target = target_result.get("suggested_target")

    # Step 2: Generate compounds using the identified target
    if target and isinstance(target, str) and len(target.strip()) > 0:
        compounds_result = compound_generator.generate_compounds(target)
        return {
            "disease": disease,
            "identified_target": target,
            "generated_compounds": compounds_result.get("generated_compounds", [])
        }
    else:
        return {
            "disease": disease,
            "error": "No target identified for the given disease."
        }
