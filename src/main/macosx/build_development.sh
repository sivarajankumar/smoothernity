rm ../../../../build/macosx/Development/Smoothernity.app/Contents/MacOS/Smoothernity
xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Development build
