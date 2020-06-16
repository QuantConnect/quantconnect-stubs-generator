# Lean Python Generator

After seeing QuantConnect create the [QuantConnect/quantconnect-lean](https://github.com/QuantConnect/quantconnect-lean) project, I challenged myself to do the same thing (generating Python type hints based on [QuantConnect/Lean's](https://github.com/QuantConnect/Lean) C# codebase) for the heck of it. The resulting project is capable of converting C# classes/structs/enums/interfaces/fields/properties/methods to Python classes/members with the correct type conversions, decorators, generics and documentation.
