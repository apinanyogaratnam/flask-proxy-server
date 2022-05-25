# Flask Proxy Server

A proxy server that can be used to forward requests to a Flask application to allow cross-origin requests.

## Table of Contents

<!-- - [Installation](#installation) -->
- [Usage](#usage)
<!-- - [Support](#support) -->
<!-- - [Contributing](#contributing) -->

<!-- ## Installation

Download to your project directory, add `README.md`, and commit:

```sh
curl -LO http://git.io/Xy0Chg
git add README.md
git commit -m "Use README Boilerplate"
``` -->

## Usage

`GET /proxy?url=https://httpbin.org/ip`

Make a request to the proxy server:

### Python
```python
import requests

response = requests.get('http://localhost:8000/proxy?url=https://httpbin.org/ip')

print(response.json())
```

### ES6 Js
```js
import axios from 'axios';

const getResponse = async () => {
  var response = await axios.get('https://httpbin.org/ip');
  return response.data;
}

const logData = async () => {
    console.log(await getResponse())
}

logData();
```

<!-- - Name
- Description
- Installation instructions
- Usage instructions
- Support instructions
- Contributing instructions
- Licence

Feel free to remove any sections that aren't applicable to your project.

## Support

Please [open an issue](https://github.com/fraction/readme-boilerplate/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/fraction/readme-boilerplate/compare/). -->
