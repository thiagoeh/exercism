# Installing .Net Core on Ubuntu

Currently exercism.io does'nt provide guidance on the installation of .Net, to be able to build in C#.

To reduce the chances of having some incompatibility between the proposed exercises and the Mono .net implementation, I've chosed to use .Net Core.

The installation instrutions for Ubuntu 16.04 (which is the release I currently use) are **[here]**(https://www.microsoft.com/net/learn/get-started/linux/ubuntu16-04)

Except for some temporary DNS resolution failures on `packages.microsoft.com` (maybe an issue on the infrastructure on my side), the default installation procedure worked just fine.



# .NET Core documentation

- [.NET Core docs](https://aka.ms/dotnet-docs)
- [dotnet cli](https://aka.ms/dotnet-cli-docs)
- [Getting started with .NET Core on Windows/Linux/macOS using the command line](https://docs.microsoft.com/en-us/dotnet/core/tutorials/using-with-xplat-cli)


# Development workflow for csharp exercises

Git commit steps are being ommited.

1. Run `exercism fetch csharp`

1. Read respective exercise `README.md` and test suite
1. Modify the `<exercise>.cs` code file aiming to fulfill the tests
1. Run `dotnet test`
