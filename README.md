# Neko-ConfigGrabber
Eat Telegram Xray Configs Like a Neko

## How to use
1. Fork this repository and make sure the repository is **private**.
2. Obtain your Telegram API ID and hash from my.telegram.org
   
**windows and linux :**
   
  3. Download [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) From Official Websites.
  
  4. Clone your private repository to your device.
  
  5. Edit lines 10-11 of `Grabber.py` with your Telegram API ID and hash.
     
  6. Edit line 12 of `Grabber.py` with your config file URL (you can see `source.conf.example` for the config file structure).
     
  7. Run `Grabber.py` on your PC and complete the initial setup (enter your mobile number and OTP code).
     
     ```
     pip install telethon requests
     python Grabber.py
     ```
     
  8. Commit the new files to your repository and enable read and write permissions for GitHub Actions in the repository settings.

     ```
     git add -A && git commit -m "config file edited" && git push
     ```

**android (termux) :**

  3. install Git and Python.

     ```
     apt update
     apt upgrade
     pkg install git
     pkg install python
     ```
     
  4. Clone your private repository to your device.

     ```
     git clone https://github.com/NekoHanaku/Neko-ConfigGrabber.git
     cd Neko-ConfigGrabber
     ```
     
  5. Edit lines 10-11 of `Grabber.py` with your Telegram API ID and hash.
  6. Edit line 12 of `Grabber.py` with your config file URL (you can see `source.conf.example` for the config file structure).
  7. Run `Grabber.py` on your PC and complete the initial setup (enter your mobile number and OTP code).

     ```
     pip install telethon requests
     python Grabber.py
     ```

  8. Commit the new files to your repository and enable read and write permissions for GitHub Actions in the repository settings.
      
      ```
      git add -A && git commit -m "config file edited" && git push
      ```




**Done.**

Now you will get the configs in the configs.json file Every 3 Hours.

## TODO
1. Add support for private channels and groups.
2. Add JSON configs support.

## Disclaimer

Please note that after running `Grabber.py`, the repository will contain personal configuration files. Ensure that your repository remains private to protect your sensitive information. **Do not share or distribute your repository.**

No Warranty: This project is provided "as is" without any warranty of any kind, either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The entire risk as to the quality and performance of the project is with you.

No Liability: In no event shall the authors be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the project or the use or other dealings in the project.

## License

This project is licensed under the GPL-3.0 license. See the LICENSE file for details.
