# Auto Batch Configuration
# Copy this to auto_batch_config.py and customize as needed

# Default folders - these override the SSOT configuration if uncommented
# DEFAULT_PDF_FOLDER = "examples/pdfs"
# DEFAULT_OUTPUT_FOLDER = "outputs/converted"

# Processing settings
TEMPERATURE = 0.05  # Lower = more consistent
MAX_TOKENS = 8192   # Higher = more complete output
DPI = 200          # Image quality (200 is good balance)

# Monitoring settings
CHECK_INTERVAL = 30  # Seconds between status checks
MAX_WAIT_TIME = 3600  # Maximum wait time in seconds (1 hour)

# Cleanup settings
AUTO_CLEANUP = True  # Automatically clean temp files
KEEP_TEMP_IMAGES = False  # Keep extracted page images

# Cost alert thresholds
COST_WARNING_THRESHOLD = 1.00  # Warn if estimated cost > $1.00
COST_ALERT_THRESHOLD = 5.00    # Alert if estimated cost > $5.00

# Output organization
CREATE_SESSION_FOLDERS = True  # Create timestamped session folders
INCLUDE_MASTER_DOCUMENT = True  # Create combined master document
DETAILED_COST_REPORTS = True   # Include detailed per-page cost analysis
