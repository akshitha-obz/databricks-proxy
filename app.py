# Add error handling for Databricks job run API
def handle_job_run_error(error):
    logging.error(f"Job Run Error: {error}")
    return {
        "status": "error",
        "message": str(error)
    }
