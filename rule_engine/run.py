import os
import logging
from app import create_app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def configure_app(app):
    """Configure the Flask application."""
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    app.config['DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///default.db')

    # Additional configuration can be added here
    logger.info("Application configured with SECRET_KEY and DATABASE_URI.")

def main():
    """Main entry point for the application."""
    app = create_app()
    configure_app(app)

    logger.info("Starting the Flask application...")
    
    # Run the application
    app.run(debug=True, host='127.0.0.1', port=int(os.getenv('PORT', 4444)))

if __name__ == "__main__":
    main()
