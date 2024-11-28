
def generate_report(response_post, response_get, validation_status):
    report = {
        "POST Response": response_post.json(),
        "GET Response": response_get.json(),
        "Validation Status": "Success" if validation_status else "Failed"
    }
    return report
