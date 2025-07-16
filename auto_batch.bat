@echo off
REM Auto Batch PDF Converter - Windows Batch Script
REM Usage: auto_batch.bat [pdf_folder] [output_folder]

echo 🤖 Auto Batch PDF Converter for Windows
echo.

if "%1"=="" (
    echo Using default folders: examples\pdfs -^> outputs\converted_markdown
    python -m batch.auto_batch
) else if "%2"=="" (
    echo Using PDF folder: %1 -^> outputs\converted_markdown
    python -m batch.auto_batch "%1"
) else (
    echo Using folders: %1 -^> %2
    python -m batch.auto_batch "%1" "%2"
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
