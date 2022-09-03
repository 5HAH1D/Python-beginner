"""
This Python script is to test the internet speed over the best servers,
only a module to download is 'speedtest-cli'
"""
import speedtest


def TestSpeed():
    # assigning function to variable for later use
    test = speedtest.Speedtest()
    # Get details about best servers
    test.get_best_server()
    # Check for upload speed
    test.upload()
    # Check for download speed
    test.download()
    # return results to function
    return test.results.dict()


save = input("Do You want to save the results in File? (y/n): ")
print("\nPlease wait while data is being processed...\n")
for i in range(3):
    Results = TestSpeed()
    print("Results for Test #" + str(i+1))
    print(Results)
    try:
        if save == "y" or "Y":
            with open("Results.txt", 'a') as f:
                test_no = i+1
                f.write("Results for Test #" + str(test_no) + "\n")
                f.write(str(Results))
                f.write("\n")
        else:
            exit()
    except Exception as e:
        print(e)
exit()
