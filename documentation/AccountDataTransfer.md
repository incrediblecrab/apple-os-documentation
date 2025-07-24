# Account Data Transfer

Download App Store information and app-install activity on behalf of your app's users.

**Platforms:** Account Data Transfer 1.0+

## Overview

Use the Account Data Transfer web API to request and download App Store information and app-install activity data about your app's users. The data available relates to a user's use of Apple's App Store and includes information such as previous transactions and downloads.

To access the data, you need to acquire an access token with the appstore-user-profile read-only scope, and at least one of these scopes:

- appstore-info-readonly
- app-install-activity-readonly

You also need to supply the query parameter consent_mode, with the value auth3p, in your call to Request an authorization.

To get permission for your App ID or Services ID to request these scopes, follow the instructions at Account & Organizational Data Sharing.

**Note**: This API returns account data about users in the EU and UK. If you are an app developer and need to transfer data related to App Store activity and app-install activity for your app instead, use App Data Transfer. If you request access to the Account Data Transfer API, and Apple grants your request, you don't need to supply the consent_mode query parameter when you request an authorization token for the App Data Transfer API.

If you have any questions about the data made available in this API, including about how Apple applies privacy measures to protect user privacy and complies with legal obligations, contact Apple through Feedback Assistant by selecting the following option:

Developer Tools & Resources > Account Data Transfer API > Data Request

Learn more about how to use Feedback Assistant.

### Set required HTTP headers

When you make requests for someone's App Store information and app-install activity, using any of the endpoints listed below, set the following HTTP headers:

**Authorization**  
Set the value to Bearer <ACCESS_TOKEN> to assert that your app is authorized to fetch data with the appstore-info-readonly scope or app-install-activity-readonly scope.

**X-Apple-Transaction-Id**  
Set the value to a UUID that uniquely identifies the request. If you need to contact Apple to get support, quote the UUID of the request for which you need help.

### Submit a request

Make an HTTP POST request to the Submit request endpoint, requesting the app-store data type. To make a one-time request, set the mode key to ONE_TIME. To make recurring requests, use one of the following values:

**DAILY_30**  
One recurring request every day for 30 days

**WEEKLY_180**  
One recurring request every week for 180 days

The Apple server returns a request ID, which you use when you get the request status, request download URLs, or cancel the request. For recurring requests, the Apple server returns a request ID, along with the parent ID that identifies the series of recurring requests.

The response from the server also contains a statusCheckDelay, which is the number of seconds you need to wait before checking the status of the request. You can cancel a request before this time by making a POST request to the Cancel request endpoint.

If you submit a recurring request and don't resubmit the recurring instances, for example, you request a DAILY_30 recurrence and don't resubmit the request each subsequent day, the recurring request expires and you need to submit another request.

### Find the request status

The data corresponding to the request you submitted isn't available immediately. After the status-check delay expires, make a GET request to Get one-time request status or Get recurring request status, including the request identifier in the path.

If the job status is completed or completed_with_error, the data associated with the request is ready to download.

### Transfer data

Get the download URLs for a completed request by making a GET request to Get one-time request download URLs or Get recurring request download URLs, including the request identifier in the path.

The response contains a list of URLs to which you make GET requests, to retrieve the person's data.

Download URLs are available for 3 days after the download request completes. The URLs you receive are valid for 15 minutes after you request them.

For information on the content and terms used in the files you download, see Data and Privacy.

### Resubmit recurring requests

Enqueue the next instance of a recurring request by making a POST request to the Resubmit request endpoint, passing the parent request identifier and the request identifier of the most recent instance.

The server's response contains the request identifier of the new request, and a delay to wait before you can check the new request's status.

## Topics

### Request creation
- **Submit request** - Starts preparing someone's data for download.
- **JobSubmission** - An object that describes a submission that requests someone's data.
- **CreatedJob** - An object that represents a newly created download request.
- **Resubmit request** - Enqueue the next instance of a recurring request.
- **ResubmissionRequest** - An object that describes a request to resubmit a recurring download request.
- **ResubmissionResponse** - An object that represents a resubmitted recurring download request.

### Status
- **Get one-time request status** - Find the status of a one-time download request.
- **Get recurring request status** - Get the status of an instance of a recurring download request.
- **RequestStatus** - An object that represents the status of a download request.

### Downloads
- **Get one-time request download URLs** - Get URLs to retrieve someone's data.
- **Get recurring request download URLs** - Get URLs to download a snapshot of someone's data from a recurring series.
- **DownloadLinks** - An object that contains URLs to download someone's account data.
- **DownloadError** - An object that describes an error the server encounters preparing download URLs for a request.

### Cancellation
- **Cancel request** - Tells the server to stop processing an active request.
- **CancellationRequest** - An object that identifies a one-time request, or an individual instance of a recurring request, to cancel.
- **CancellationResponse** - An object that describes the outcome of canceling a download request.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AccountDataTransfer)*