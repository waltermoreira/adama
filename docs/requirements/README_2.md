## Random notes on the architecture

(ADAMA code is at http://github.com/waltermoreira/adama)

- As part of the registration procedure, the service (ADAMA) builds a
  Docker container with the user's code.

- The user's code is only a function `f: JSON -> JSON` that access the
  third party service with its specific protocol.

- The container handles all the communication with the queue. The
  user's code **does not** need to interact with anything other than
  the URL of the third party service.

- Pagination and count:

  - If the third party service supports pagination, the user's code
    declares at registration time whether it will handle it through
    the function `f`. Otherwise, ADAMA will handle pagination and count
    through caching.

![architecture](https://github.com/Arabidopsis-Information-Portal/araport_data_api_design/raw/master/architecture/workers.png)
