# Configuration

Since version 0.10, ceria reads configuration from `$XDG_CONFIG_HOME/ceria/config.toml`.

Things that can be configured are:

- key bindings
- colors

Upon running ceria version 0.10 or above,
the configuration will be created with default values
if it doesn't already exist.

The format of the configuration file
is [TOML](https://github.com/toml-lang/toml).

You can bind several key to a single action if you want:

```toml
FOLLOW_ROW = "F"    # only one key
HELP = ["F1", "?"]  # multiple keys
```