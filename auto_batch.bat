@echo off
REM Auto Batch PDF Converter - Windows Batch Script
REM Usage: auto_batch.bat [pdf_folder] [output_folder]

echo 🤖 Auto Batch PDF Converter for Windows
echo.

if "%1"=="" (
    echo Using default folders: pdfs -^> converted_markdown
    python auto_batch.py
) else if "%2"=="" (
    echo Using PDF folder: %1 -^> converted_markdown
    python auto_batch.py "%1"
) else (
    echo Using folders: %1 -^> %2
    python auto_batch.py "%1" "%2"
)

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Processing completed successfully!
    echo Check the converted_markdown folder for results.
) else (
    echo.
    echo ❌ Processing failed. Check the output above for details.
)

pause
