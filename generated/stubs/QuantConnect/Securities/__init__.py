import QuantConnect
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Securities.Interfaces
import QuantConnect.Securities.Volatility
import abc
import enum
import typing


INotifyCollectionChanged = typing.Any
IDynamicMetaObjectProvider = typing.Any
System_EventArgs = typing.Any
System_IEquatable = typing.Any


QuantConnect_Securities_IndicatorVolatilityModel_T = typing.TypeVar('QuantConnect_Securities_IndicatorVolatilityModel_T')


class MarketHoursDatabase:
    """
    Provides access to exchange hours and raw data times zones in various markets
    """


    class Entry:
        """
        Represents a single entry in the MarketHoursDatabase
        """


    class AlwaysOpenMarketHoursDatabaseImpl(MarketHoursDatabase):
        """
        This class has no documentation.
        """


class ISecuritySeeder(metaclass=abc.ABCMeta):
    """
    Used to seed the security with the correct price
    """


class SecuritySeeder:
    """
    Provides access to a null implementation for ISecuritySeeder
    """


class GetMaximumOrderQuantityResult:
    """
    Contains the information returned by IBuyingPowerModel.GetMaximumOrderQuantityForTargetBuyingPower
    and  IBuyingPowerModel.GetMaximumOrderQuantityForDeltaBuyingPower
    """


class CashAmount:
    """
    Represents a cash amount which can be converted to account currency using a currency converter
    """


class SecurityHolding:
    """
    SecurityHolding is a base class for purchasing and holding a market item which manages the asset portfolio
    """


class ISecurityProvider(metaclass=abc.ABCMeta):
    """
    Represents a type capable of fetching the holdings for the specified symbol
    """


class SecurityProviderExtensions:
    """
    Provides extension methods for the ISecurityProvider interface.
    """


class IDerivativeSecurity(metaclass=abc.ABCMeta):
    """
    Defines a security as a derivative of another security
    """


class HasSufficientBuyingPowerForOrderParameters:
    """
    Defines the parameters for IBuyingPowerModel.HasSufficientBuyingPowerForOrder
    """


class IDerivativeSecurityFilter(metaclass=abc.ABCMeta):
    """
    Filters a set of derivative symbols using the underlying price data.
    """


class Security(QuantConnect.Interfaces.ISecurityPrice):
    """
    A base vehicle properties class for providing a common interface to all assets in QuantConnect.
    """


class BuyingPowerParameters:
    """
    Defines the parameters for IBuyingPowerModel.GetBuyingPower
    """


class GetMaximumOrderQuantityForDeltaBuyingPowerParameters:
    """
    Defines the parameters for IBuyingPowerModel.GetMaximumOrderQuantityForDeltaBuyingPower
    """


class BuyingPowerModel(IBuyingPowerModel):
    """
    Provides a base class for all buying power models
    """


class CashBuyingPowerModel(BuyingPowerModel):
    """
    Represents a buying power model for cash accounts
    """


class ImmediateSettlementModel(ISettlementModel):
    """
    Represents the model responsible for applying cash settlement rules
    """


class InitialMarginRequiredForOrderParameters:
    """
    Defines the parameters for BuyingPowerModel.GetInitialMarginRequiredForOrder
    """


class AdjustedPriceVariationModel(IPriceVariationModel):
    """
    Provides an implementation of IPriceVariationModel
    for use when data is DataNormalizationMode.Adjusted.
    """


class HasSufficientBuyingPowerForOrderResult:
    """
    Contains the information returned by IBuyingPowerModel.HasSufficientBuyingPowerForOrder
    """


class BuyingPowerModelExtensions:
    """
    Provides extension methods as backwards compatibility shims
    """


class SecurityExchangeHours:
    """
    Represents the schedule of a security exchange. This includes daily regular and extended market hours
    as well as holidays, early closes and late opens.
    """


class SecurityCache:
    """
    Base class caching caching spot for security data and any other temporary properties.
    """


class SecurityPortfolioModel(ISecurityPortfolioModel):
    """
    Provides a default implementation of ISecurityPortfolioModel that simply
    applies the fills to the algorithm's portfolio. This implementation is intended to
    handle all security types.
    """


class EquityPriceVariationModel(SecurityPriceVariationModel):
    """
    Provides an implementation of IPriceVariationModel
    for use in defining the minimum price variation for a given equity
    under Regulation NMS – Rule 612 (a.k.a – the “sub-penny rule”)
    """


class SecurityManager(QuantConnect.ExtendedDictionary[Security], typing.Dict[QuantConnect.Symbol, Security], INotifyCollectionChanged):
    """
    Enumerable security management class for grouping security objects into an array and providing any common properties.
    """


class FuncSecurityInitializer(ISecurityInitializer):
    """
    Provides a functional implementation of ISecurityInitializer
    """


class GetMaximumOrderQuantityForTargetBuyingPowerParameters:
    """
    Defines the parameters for IBuyingPowerModel.GetMaximumOrderQuantityForTargetBuyingPower
    """


class DynamicSecurityData(IDynamicMetaObjectProvider):
    """
    Provides access to a security's data via it's type. This implementation supports dynamic access
    by type name.
    """


class PatternDayTradingMarginModel(SecurityMarginModel):
    """
    Represents a simple margining model where margin/leverage depends on market state (open or close).
    During regular market hours, leverage is 4x, otherwise 2x
    """


class SecurityCacheDataStoredEventArgs(System_EventArgs):
    """
    Event args for SecurityCache.DataStored event
    """


class BuyingPower:
    """
    Defines the result for IBuyingPowerModel.GetBuyingPower
    """


class ICurrencyConverter(metaclass=abc.ABCMeta):
    """
    Provides the ability to convert cash amounts to the account currency
    """


class LocalMarketHours:
    """
    Represents the market hours under normal conditions for an exchange and a specific day of the week in terms of local time
    """


class SecurityService(QuantConnect.Interfaces.ISecurityService):
    """
    This class implements interface ISecurityService providing methods for creating new Security
    """


class ISecurityInitializer(metaclass=abc.ABCMeta):
    """
    Represents a type capable of initializing a new security
    """


class SecurityInitializer:
    """
    Provides static access to the Null security initializer
    """


class ISettlementModel(metaclass=abc.ABCMeta):
    """
    Represents the model responsible for applying cash settlement rules
    """


class ISecurityPortfolioModel(metaclass=abc.ABCMeta):
    """
    Performs order fill application to portfolio
    """


class IBuyingPowerModel(metaclass=abc.ABCMeta):
    """
    Represents a security's model of buying power
    """


class IDerivativeSecurityFilterUniverse(typing.List[QuantConnect.Symbol], metaclass=abc.ABCMeta):
    """
    Represents derivative symbols universe used in filtering.
    """


class SecurityDataFilter(QuantConnect.Securities.Interfaces.ISecurityDataFilter):
    """
    Base class implementation for packet by packet data filtering mechanism to dynamically detect bad ticks.
    """


class MarketHoursState(enum.Enum):
    """
    Specifies the open/close state for a MarketHoursSegment
    """


class Cash:
    """
    Represents a holding of a currency in cash.
    """


class ReservedBuyingPowerForPositionParameters:
    """
    Defines the parameters for IBuyingPowerModel.GetReservedBuyingPowerForPosition
    """


class FuncSecurityDerivativeFilter(IDerivativeSecurityFilter):
    """
    Provides a functional implementation of IDerivativeSecurityFilter
    """


class IOrderEventProvider(metaclass=abc.ABCMeta):
    """
    Represents a type with a new OrderEvent event EventHandler.
    """


class MarketHoursSegment:
    """
    Represents the state of an exchange during a specified time range
    """


class GetMinimumPriceVariationParameters:
    """
    Defines the parameters for IPriceVariationModel.GetMinimumPriceVariation
    """


class IRegisteredSecurityDataTypesProvider(metaclass=abc.ABCMeta):
    """
    Provides the set of base data types registered in the algorithm
    """


class SecurityPortfolioManager(QuantConnect.ExtendedDictionary[SecurityHolding], typing.Dict[QuantConnect.Symbol, SecurityHolding], ISecurityProvider):
    """
    Portfolio manager class groups popular properties and makes them accessible through one interface.
    It also provide indexing by the vehicle symbol to get the Security.Holding objects.
    """


class DelayedSettlementModel(ISettlementModel):
    """
    Represents the model responsible for applying cash settlement rules
    """


class CashBook(typing.Dict[str, Cash], ICurrencyConverter):
    """
    Provides a means of keeping track of the different cash holdings of an algorithm
    """


    class UpdateType(enum.Enum):
        """
        The different types of Updated events
        """


class BrokerageModelSecurityInitializer(ISecurityInitializer):
    """
    Provides an implementation of ISecurityInitializer that initializes a security
    by settings the Security.FillModel, Security.FeeModel,
    Security.SlippageModel, and the Security.SettlementModel properties
    """


class AccountEvent:
    """
    Messaging class signifying a change in a user's account
    """


class SecurityDatabaseKey(System_IEquatable):
    """
    Represents the key to a single entry in the MarketHoursDatabase or the SymbolPropertiesDatabase
    """


class FuncSecuritySeeder(ISecuritySeeder):
    """
    Seed a security price from a history function
    """


class SecurityTransactionManager(IOrderProvider):
    """
    Algorithm Transactions Manager - Recording Transactions
    """


class IBaseCurrencySymbol(metaclass=abc.ABCMeta):
    """
    This class has no documentation.
    """


class SecurityCacheProvider:
    """
    A helper class that will provide SecurityCache instances
    """


class IMarginCallModel(metaclass=abc.ABCMeta):
    """
    Represents the model responsible for picking which orders should be executed during a margin call
    """


class MarginCallModel:
    """
    Provides access to a null implementation for IMarginCallModel
    """


class SecurityExchange:
    """
    Base exchange class providing information and helper tools for reading the current exchange situation
    """


class AccountCurrencyImmediateSettlementModel(ISettlementModel):
    """
    Represents the model responsible for applying cash settlement rules
    """


class IdentityCurrencyConverter(ICurrencyConverter):
    """
    Provides an implementation of ICurrencyConverter that does NOT perform conversions.
    This implementation will throw if the specified cashAmount is not in units of account currency.
    """


class SecurityMarginModel(BuyingPowerModel):
    """
    Represents a simple, constant margin model by specifying the percentages of required margin.
    """


class UnsettledCashAmount:
    """
    Represents a pending cash amount waiting for settlement time
    """


class ReservedBuyingPowerForPosition:
    """
    Defines the result for IBuyingPowerModel.GetReservedBuyingPowerForPosition
    """


class RegisteredSecurityDataTypesProvider(IRegisteredSecurityDataTypesProvider):
    """
    Provides an implementation of IRegisteredSecurityDataTypesProvider that permits the
    consumer to modify the expected types
    """


class IOrderProcessor(IOrderProvider, metaclass=abc.ABCMeta):
    """
    Represents a type capable of processing orders
    """


class DefaultMarginCallModel(IMarginCallModel):
    """
    Represents the model responsible for picking which orders should be executed during a margin call
    """


class SymbolPropertiesDatabase:
    """
    Provides access to specific properties for various symbols
    """


class CompositeSecurityInitializer(ISecurityInitializer):
    """
    Provides an implementation of ISecurityInitializer that executes
    each initializer in order
    """


class SecurityPriceVariationModel(IPriceVariationModel):
    """
    Provides default implementation of IPriceVariationModel
    for use in defining the minimum price variation.
    """


class IPriceVariationModel(metaclass=abc.ABCMeta):
    """
    Gets the minimum price variation of a given security
    """


class IOrderProvider(metaclass=abc.ABCMeta):
    """
    Represents a type capable of fetching Order instances by its QC order id or by a brokerage id
    """


class OrderProviderExtensions:
    """
    Provides extension methods for the IOrderProvider interface
    """


class UniverseManager(typing.Dict[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe], INotifyCollectionChanged):
    """
    Manages the algorithm's collection of universes
    """


class ErrorCurrencyConverter(ICurrencyConverter):
    """
    Provides an implementation of ICurrencyConverter for use in
    tests that don't depend on this behavior.
    """


class SymbolProperties:
    """
    Represents common properties for a specific security, uniquely identified by market, symbol and security type
    """


class IndicatorVolatilityModel(typing.Generic[QuantConnect_Securities_IndicatorVolatilityModel_T], IVolatilityModel):
    """
    Provides an implementation of IVolatilityModel that uses an indicator
    to compute its value
    """


class IVolatilityModel(metaclass=abc.ABCMeta):
    """
    Represents a model that computes the volatility of a security
    """


class VolatilityModel:
    """
    Provides access to a null implementation for IVolatilityModel
    """


class RelativeStandardDeviationVolatilityModel(QuantConnect.Securities.Volatility.BaseVolatilityModel):
    """
    Provides an implementation of IVolatilityModel that computes the
    relative standard deviation as the volatility of the security
    """


class StandardDeviationOfReturnsVolatilityModel(QuantConnect.Securities.Volatility.BaseVolatilityModel):
    """
    Provides an implementation of IVolatilityModel that computes the
    annualized sample standard deviation of daily returns as the volatility of the security
    """


class OptionFilterUniverse(IDerivativeSecurityFilterUniverse):
    """
    Represents options symbols universe used in filtering.
    """


    class Type(enum.Enum):
        """
        Defines listed option types
        """


class OptionFilterUniverseEx:
    """
    Extensions for Linq support
    """


class FutureFilterUniverse(IDerivativeSecurityFilterUniverse):
    """
    Represents futures symbols universe used in filtering.
    """


class FutureFilterUniverseEx:
    """
    Extensions for Linq support
    """


class Futures:
    """
    Futures static class contains shortcut definitions of major futures contracts available for trading
    """


    class Grains:
        """
        Grains and Oilseeds group
        """


    class Currencies:
        """
        Currencies group
        """


    class Energies:
        """
        Energies group
        """


    class Financials:
        """
        Financials group
        """


    class Indices:
        """
        Indices group
        """


    class Forestry:
        """
        Forestry group
        """


    class Meats:
        """
        Meats group
        """


    class Metals:
        """
        Metals group
        """


    class Softs:
        """
        Softs group
        """


    class Dairy:
        """
        Dairy group
        """


class FutureExpirationCycles:
    """
    Static class contains definitions of popular futures expiration cycles
    """


