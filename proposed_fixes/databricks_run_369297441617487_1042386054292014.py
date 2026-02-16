"""
Fixed version of the code to handle errors properly instead of using sys.exit(1)
"""

import requests
import logging
from typing import Optional, Dict, Any

class JobExecutionError(Exception):
    """Custom exception for job execution errors"""
    pass

def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def make_api_request(url: str, api_key: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Make API request with proper error handling
    
    Args:
        url: API endpoint URL
        api_key: Authentication key
        payload: Request payload
    
    Returns:
        API response as dictionary
    
    Raises:
        JobExecutionError: If API request fails
    """
    try:
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        return response.json()
    
    except requests.RequestException as e:
        raise JobExecutionError(f"API request failed: {str(e)}")

def main(api_url: str, api_key: str, job_id: str, run_id: str) -> None:
    """
    Main execution function with proper error handling
    
    Args:
        api_url: API endpoint URL
        api_key: Authentication key
        job_id: Databricks job ID
        run_id: Databricks run ID
    """
    logger = setup_logging()
    
    try:
        logger.info(f"Starting job execution for job_id: {job_id}, run_id: {run_id}")
        
        # Validate inputs
        if not all([api_url, api_key, job_id, run_id]):
            raise ValueError("Missing required parameters")
        
        payload = {
            "job_id": job_id,
            "run_id": run_id
        }
        
        # Make API request
        response = make_api_request(api_url, api_key, payload)
        
        logger.info(f"Successfully processed job. Response: {response}")
        
    except ValueError as e:
        logger.error(f"Input validation error: {str(e)}")
        raise
    except JobExecutionError as e:
        logger.error(f"Job execution failed: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise

if __name__ == "__main__":
    # Get parameters from notebook context
    api_url = dbutils.widgets.get("api-url")
    api_key = dbutils.widgets.get("api-key")
    job_id = dbutils.widgets.get("job-id")
    run_id = dbutils.widgets.get("run-id")
    
    try:
        main(api_url, api_key, job_id, run_id)
    except Exception as e:
        # Log the error but don't use sys.exit
        logging.error(f"Job failed: {str(e)}")
        raise  # Re-raise the exception for Databricks to handle