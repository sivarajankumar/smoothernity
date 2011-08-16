rm ../../../../build/macosx/Development/Smoothernity.app/Contents/MacOS/Smoothernity
rm ./smoothernity.xcodeproj/*.pbxuser
rm ./smoothernity.xcodeproj/*.mode1v3
xcodebuild -project smoothernity.xcodeproj -target "smoothernity" -configuration Development build
