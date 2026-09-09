# Notary API

Submit your macOS software for notarization through a REST API.

**Service API version:** Notary API 2.0.0. This is not an Apple OS deployment version.

## Overview

Notarization gives people confidence that your Developer ID-signed macOS software has been checked by Apple for malicious code. In addition to interacting with the notary service through Xcode or the notarytool command-line utility, you can bypass notarytool and interact directly with the service through its REST API. The Notary API is helpful for instances where you need to avoid a macOS dependency when uploading your app to the notary service, and provides endpoints that enable you to:

- Prepare the notary service to receive a new version of your software, and get credentials that you use to upload your software to an Amazon S3 endpoint.
- Check the status of a submission.
- Retrieve a log file that provides details about a submission.
- Get a list of your team's previous submissions.

To learn how notarization works, see Notarizing macOS software before distribution. For details about using the notary service REST API to upload your software, see Submitting software for notarization over the web.

## Topics

### Essentials
- [Submitting software for notarization over the web](https://developer.apple.com/documentation/notaryapi/submitting-software-for-notarization-over-the-web) - Replace the upload/status portions of a `notarytool` workflow with REST calls; building, signing and other workflow requirements are separate.

### Software submission
- [Submit Software](https://developer.apple.com/documentation/notaryapi/submit-software) - Prepare a submission and obtain upload information; this request does not itself upload the software.
- **NewSubmissionRequest** - Data that you provide when starting a submission to the notary service.
- **NewSubmissionResponse** - The notary service's response to a software submission.

### Notarization results
- [Get Submission Status](https://developer.apple.com/documentation/notaryapi/get-submission-status) - Fetch the status of a software notarization submission.
- **SubmissionResponse** - The notary service's response to a request for the status of a submission.
- [Get Submission Log](https://developer.apple.com/documentation/notaryapi/get-submission-log) - Fetch details about a single completed notarization.
- **SubmissionLogURLResponse** - The notary service's response to a request for the log information about a completed submission.

### History
- [Get Previous Submissions](https://developer.apple.com/documentation/notaryapi/get-previous-submissions) - Fetch a list of your team's previous notarization submissions.
- **SubmissionListResponse** - The notary service's response to a request for information about your team's previous submissions.

### Errors
- **ErrorResponse** - The notary service's response when an error occurs.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/NotaryAPI)*
