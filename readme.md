# GitSearch ![Stars](https://img.shields.io/github/stars/realTristan/GitSearch?color=brightgreen) ![Watchers](https://img.shields.io/github/watchers/realTristan/GitSearch?label=Watchers)
![102393310-07478b80-3f8d-11eb-84eb-392d555ebd29](https://user-images.githubusercontent.com/75189508/192170833-83339980-9fc0-48ab-9334-7c650cdd6123.png)

<h3>About</h3>
Gitsearch is an easy-to-use python script that produces a list of github users based on the inputted user. The program utilizes the github api for finding the users based off the provided users followings/followers.

<h3>Showcase</h3>
```json
    "https://api.github.com/users/defunkt": {
        "came_from": [
            "https://api.github.com/users/esin",
            "https://api.github.com/users/BinaryWorld0101201",
            "https://api.github.com/users/realtristan"
        ],
        "data": [
            null,
            "\ud83c\udf54",
            null,
            "Chris Wanstrath",
            null,
            "http://chriswanstrath.com/",
            null
        ]
    },
    "https://api.github.com/users/blanu": {
        "came_from": [
            "https://api.github.com/users/uberspot",
            "https://api.github.com/users/BinaryWorld0101201",
            "https://api.github.com/users/realtristan"
        ],
        "data": [
            null,
            null,
            null,
            "Dr. Brandon Wiley",
            "Austin, Texas",
            "https://OperatorFoundation.org/",
            "Operator Foundation"
        ]
    }
}
```

# License
MIT License

Copyright (c) 2022 Tristan Simpson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
