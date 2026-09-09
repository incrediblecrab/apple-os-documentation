#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT="${1:?Provide a new output directory for build and test artifacts}"
EXPECTED_XCODE_MAJOR="${EXPECTED_XCODE_MAJOR:-26}"
PROJECT="$ROOT/os26-liquid-glass-example/Landmarks/Landmarks.xcodeproj"

xcodebuild -version
xcrun swift --version
xcrun --sdk macosx --show-sdk-version
ACTUAL_XCODE_MAJOR="$(xcodebuild -version | awk '$1 == "Xcode" { split($2, parts, "."); print parts[1] }')"
if [ "$ACTUAL_XCODE_MAJOR" != "$EXPECTED_XCODE_MAJOR" ]; then
    printf 'Expected Xcode %s, selected Xcode %s. Set DEVELOPER_DIR explicitly.\n' \
        "$EXPECTED_XCODE_MAJOR" "$ACTUAL_XCODE_MAJOR" >&2
    exit 1
fi
mkdir -p "$OUTPUT"

xcrun --sdk macosx swiftc -swift-version 6 -typecheck \
    "$ROOT/os26-liquid-glass-example/Snippets/LiquidGlass.swift" \
    "$ROOT/os26-liquid-glass-example/Snippets/WeakLet.swift"

xcodebuild -quiet -project "$PROJECT" -scheme Landmarks \
    -destination 'platform=macOS,arch=arm64' \
    -derivedDataPath "$OUTPUT/macos" -resultBundlePath "$OUTPUT/ModelTests.xcresult" \
    CODE_SIGNING_ALLOWED=NO test

xcrun xcresulttool get test-results summary --path "$OUTPUT/ModelTests.xcresult" \
    > "$OUTPUT/model-test-summary.json"
python3 - "$OUTPUT/model-test-summary.json" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as stream:
    result = json.load(stream)
if result["passedTests"] < 7 or result["failedTests"] or result["skippedTests"]:
    raise SystemExit("Expected at least seven passing model tests, with no failures or skips.")
print(f"Model tests passed: {result['passedTests']}")
PY

xcodebuild -quiet -project "$PROJECT" -scheme Landmarks \
    -destination 'generic/platform=iOS Simulator' \
    -derivedDataPath "$OUTPUT/ios" CODE_SIGNING_ALLOWED=NO build

printf 'Build and test artifacts: %s\n' "$OUTPUT"
