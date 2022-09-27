'''Script is to get all WIFI passwords stored on your copmuter using Python'''
# importing modules re for regular expressions and subprocess to run commands
import re
import subprocess


def show_passcode():
    # running command to get all profiles stored in computer
    # if we want to store that info set 'capture_output=True'
    # output captured will be in 'stdout' at backend in other formate (bytes), so we have to decode it
    root_command = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

    # Finding all profiles saved on computer and create group of characters until \r using re
    wifi_profiles = (re.findall("All User Profile     : (.*)\r", root_command))

    # creating a list that will contain all the profiles' data (values will be added later)
    list_of_profiles = []

    # check weather the profile name is empty or not
    if len(wifi_profiles) != 0:

        # loop for each profile name in list of profiles found
        for profile_name in wifi_profiles:
            # creating dictionary to store each profile info separately in 'list_of_profiles'
            profile = {}
            # getting info about a specific Wi-Fi profile
            profile_info = subprocess.run(["netsh", "wlan", "show", "profile", profile_name], capture_output=True).stdout.decode()
            # check if security-key is present or not
            if re.search("Security key           : Absent", profile_info):
                continue
            else:
                # If security-key is present add SSID of the Wi-Fi profile to dictionary.
                profile['SSID'] = profile_name

                profile_passcode = subprocess.run(["netsh", "wlan", "show", "profile", profile_name, "key=clear"],
                                                  capture_output=True).stdout.decode()
                passcode = re.search("Key Content            : (.*)\r", profile_passcode)
                if passcode is None:
                    profile["password"] = None
                else:
                    # The group containing password is assigned to dictionary with a key value of 'passcode'
                    profile["Passcode"] = passcode[1]
                # Dictionary containing profile info is appended to list
                list_of_profiles.append(profile)
    # Return the list_of_profiles to the function
    return list_of_profiles


if __name__ == '__main__':
    # The condition 'name == main' is only true if script is ran directly (not imported to any other script as module)
    returned_list = show_passcode()
    for index in range(len(returned_list)):
        print(returned_list[index])
