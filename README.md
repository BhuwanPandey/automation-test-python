## ⚙️ Setup Instructions

### Clone the project

```
git clone https://github.com/BhuwanPandey/automation-test-python
cd automation-test-python
```

### Create and activate a virtual environment

```
python -m venv .venv
.venv/scripts/activate
```

### Install Project Dependencies

```bash
pip install -r requirements.txt
```

## Setup Tools
Before running test, It is neccessary to setup different tools.

- [Appium](https://appium.io/docs/en/latest/quickstart/install/) `To Perform Automation test on MobileApp` <br>
    -   [ ] You can either follow `setup and configuration` steps from respective documentation or follow process mention below: <br>
        -   Download [Node.js](https://nodejs.org/en) and [npm](https://www.npmjs.com/)  version >=8 (LTS is recommended)
        -   `Appium` can be installed globally using npm as <br>
            ```
            npm install -g appium
            ```
    -   [ ] Install the UiAutomator2 Driver
        -   You can't do much with `Appium` unless you have a driver, which is an interface that allows Appium to automate a particular platform. The driver we're going to use is called the               [UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver).
        -   In addition to a working `Appium server`, we also need to set up the following:
            #### Android SDK
            -  Easiest way to set up the Android SDK requirements is to download [Android Studio](https://developer.android.com/studio)
            -  Set up the `ANDROID_HOME` environment variable to point to the directory where the Android SDK is installed. Examplepath: `C:\Users\<Username>\AppData\Local\Android\Sdk\`
            -  For more control over android device and emulator. Use `adb` ADB (Android Debug Bridge) is a command-line tool that allows developers to communicate with Android devices or     
               emulators.
            -  Add the path of the `platform-tools` folder to your system's PATH environment variable. Examplepath: `C:\Users\<Username>\AppData\Local\Android\Sdk\platform-tools`
            -  Common ADB Commands
                ```
                # List Connected Devices
                adb devices
                # Install an APK
                adb install <path-to-apk>
                # Access Device Shell
                adb shell
                ```

            #### Java JDK
            -  Install the `Java JDK` and You can download this from [Oracle](https://jdk.java.net/). Make sure you get the `JDK` and `not the JRE`.
            -  Set up the `JAVA_HOME` environment variable to point to the JDK home directory. Examplepath: `C:\ProgramFiles\Java\jdk-23\`

            #### Install the driver
            -  Before installing, make sure your `Appium server` is not running. Then run the following command:
              ```
                appium driver install uiautomator2
              ```
            #### Validating the Install
            -  To validate whether all prerequisites have been set up correctly,
              ```
              # Install doctor
              appium driver install doctor
              # Validating
              # Note: It might raise some warning but it's okay 
              appium driver doctor uiautomator2
              ```
- [Appium Inspector](https://github.com/appium/appium-inspector/releases)  `A GUI inspector for mobile app` <br>
  -  [ ] Features
      -  Specify the Appium server details
      -  Interact with the app screenshot
      -  Search for elements and interact with them
  -  Here is the screenshot, It is neccesary to start `appium server` before starting session
    ![appium_inspector](https://github.com/user-attachments/assets/6fc7950a-797f-409b-b39d-63773d44bdf8)

## 🏃‍♂️ Run the  Testcase
After installing all the required tools, Now do the following
- Open android studio emulator to see overall test interaction
- Run `appium server` in separate console and execute the below command to perform automation test
  
  ```
    pytest -x -v 
  ```
