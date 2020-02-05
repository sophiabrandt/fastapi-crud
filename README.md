<h1 align="center">Welcome to fastapi-crud 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://twitter.com/hisophiabrandt" target="_blank">
    <img alt="Twitter: hisophiabrandt" src="https://img.shields.io/twitter/follow/hisophiabrandt.svg?style=social" />
  </a>
</p>

> Example CRUD API using FastAPI

### 🏠 [Homepage](https://github.com/sophiabrandt/fastapi-crud)

The repository contains the code from [Developing and Testing an Asynchronous API with FastAPI and Pytest][testdriven], with minor modifications.

See [original repo by Michael Herman][origrepo] by Michael Herman for more information.

## Install

You'll need Docker and docker-compose.

```sh
git clone https://github.com/sophiabrandt/fastapi-crud
cd fastapi-crud
```

## Usage

```sh
docker-compose up -d --build
```

## Run tests

```sh
docker-compose exec web pytest .
```

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/sophiabrandt/fastapi-crud/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

👤 **Sophia Brandt**

- Website: https://www.sophiabrandt.com
- Twitter: [@hisophiabrandt](https://twitter.com/hisophiabrandt)
- Github: [@sophiabrandt](https://github.com/sophiabrandt)

## License

&copy; 2020 [Michael Herman][testdriven]. See [original repository][origrepo].  
Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

## Acknowledgements

The original code was written by [Michael Herman][testdriven].

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

[testdriven]: https://testdriven.io/blog/fastapi-crud/
[origrepo]: https://github.com/testdrivenio/fastapi-crud-async
