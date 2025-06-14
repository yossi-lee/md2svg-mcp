# Markdown to SVG Converter

A tool to convert Markdown text into SVG images. This tool supports various Markdown elements such as headings, lists, code blocks, and tables.

## Installation

To install this package, run the following command:

```bash
pip install markdown-to-svg
```

## Usage

To convert Markdown text to an SVG image, use the following command:

```bash
markdown-to-svg "Your Markdown text here" --output_file output.svg
```

### Example

```bash
markdown-to-svg "# Hello World\n\nThis is a *test*." --output_file example.svg
```

This will generate an SVG file named `example.svg` containing the rendered Markdown content.

## Features

- Supports headings (h1, h2)
- Supports lists (unordered)
- Supports code blocks
- Supports tables
- Customizable output file name
- SVG output with customizable dimensions and padding

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
