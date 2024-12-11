# GenAi Assessment

A production-scale application for summarizing legal questions using OpenAI's API.

## Features
- Upload CSV files containing legal questions
- Generate concise summaries with state codes (if applicable)
- Download summarized results as CSV
- Async processing with FastAPI backend
- React frontend with Tailwind CSS
- Dockerized services
- CI/CD with GitHub Actions

## Prerequisites
- Docker and Docker Compose
- Node.js 20 (for local development)
- Python 3.12 (for local development)
- OpenAI API key

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GenAi.git
   cd GenAi
   ```

2. Create and configure the `.env` file in `backend/`:
   ```
   OPENAI_API_KEY=your-openai-api-key
   ENVIRONMENT=development
   LOG_LEVEL=INFO
   ```

3. Start the services:
   ```bash
   docker-compose up --build
   ```

4. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/docs

## Development
- Backend: `cd backend && uvicorn app.main:app --reload`
- Frontend: `cd frontend && npm start`

## Testing
- Backend: `cd backend && pytest`
- Frontend: `cd frontend && npm test`

## Deployment
The project includes a GitHub Actions workflow for CI. For production deployment, consider:
- Using a managed database (e.g., PostgreSQL)
- Setting up a reverse proxy (e.g., Nginx)
- Configuring HTTPS
- Monitoring and alerting
# Add instructions for cloning, setup, and running the app
