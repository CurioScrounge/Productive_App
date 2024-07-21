[Setup]
AppName=ProductiveApp
AppVersion=1.0
DefaultDirName={pf}\ProductiveApp
DefaultGroupName=ProductiveApp
OutputDir=.
OutputBaseFilename=ProductiveAppInstaller
Compression=lzma
SolidCompression=yes

[Files]
; Include the PyInstaller executable
Source: "dist\GUI.exe"; DestDir: "{app}"; Flags: ignoreversion

; Include settings.json
Source: "settings.json"; DestDir: "{app}"; Flags: ignoreversion

; Include Tesseract OCR
Source: "Tesseract-OCR\*"; DestDir: "{app}\Tesseract-OCR"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\ProductiveApp"; Filename: "{app}\GUI.exe"
Name: "{group}\Uninstall ProductiveApp"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\GUI.exe"; Description: "{cm:LaunchProgram,ProductiveApp}"; Flags: nowait postinstall skipifsilent