from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import pandas as pd
from ...services.summarizer import generate_summaries
import logging
from pathlib import Path

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/summarize", response_class=FileResponse)
async def summarize_questions(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are allowed")
        
        # Read CSV
        content = await file.read()
        df = pd.read_csv(pd.io.common.StringIO(content.decode('utf-8')))
        if 'QuestionText' not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must contain 'QuestionText' column")
        
        questions = df['QuestionText'].dropna().tolist()
        
        # Generate summaries
        logger.info(f"Processing {len(questions)} questions")
        summaries = await generate_summaries(questions)
        
        # Save output
        output_path = Path("outputs/output.csv")
        output_path.parent.mkdir(exist_ok=True)
        summary_df = pd.DataFrame(summaries)
        summary_df.to_csv(output_path, index=False)
        
        logger.info(f"Summaries saved to {output_path}")
        return FileResponse(output_path, filename="summaries.csv")
    
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
# Implement /api/v1/summarize with CSV validation
# Add error handling for empty CSV uploads
