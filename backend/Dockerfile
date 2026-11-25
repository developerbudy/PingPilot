
# 1. Use Python 3.12 as the base image
FROM python:3.12-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy uv from its official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 4. Configure uv
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_PROJECT_ENVIRONMENT=/opt/venv

# 5. Copy dependency configuration
COPY pyproject.toml uv.lock ./

# 6. Install dependencies using uv
RUN uv sync --frozen --no-dev --no-install-project

# 7. Copy application source code
COPY app ./app

# 8. Add virtual environment to PATH
ENV PATH="/opt/venv/bin:$PATH"

# 9. Expose application port
EXPOSE 8000

# 10. Start FastAPI using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
