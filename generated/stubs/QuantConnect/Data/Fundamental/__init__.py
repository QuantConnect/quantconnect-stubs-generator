import QuantConnect.Data
import abc


class MultiPeriodField(metaclass=abc.ABCMeta):
    """
    Abstract base class for multi-period fields
    """


    class PeriodField:
        """
        This class is protected.
        
        Helper, and internal struct use to hold the values for a period.
        """


class StockType:
    """
    Helper class for the AssetClassification's StockType field AssetClassification.StockType
    """


class StyleBox:
    """
    Helper class for the AssetClassification's StyleBox field AssetClassification.StyleBox.
    For stocks and stock funds, it classifies securities according to market capitalization and growth and value factor
    """


class MorningstarEconomySphereCode:
    """
    Helper class for the AssetClassification's MorningstarEconomySphereCode field AssetClassification.MorningstarEconomySphereCode.
    """


class MorningstarSectorCode:
    """
    Helper class for the AssetClassification's MorningstarSectorCode field AssetClassification.MorningstarSectorCode.
    """


class MorningstarIndustryGroupCode:
    """
    Helper class for the AssetClassification's MorningstarIndustryGroupCode field AssetClassification.MorningstarIndustryGroupCode.
    """


class MorningstarIndustryCode:
    """
    Helper class for the AssetClassification's MorningstarIndustryCode field AssetClassification.MorningstarIndustryCode.
    """


class Period:
    """
    Period constants for multi-period fields
    """


class PeriodAsByte:
    """
    Period constants for multi-period fields as bytes
    """


class FineFundamental(QuantConnect.Data.BaseData):
    """
    Definition of the FineFundamental class
    """


class Fundamentals(FineFundamental):
    """
    Defines a merged viw of FineFundamental and CoarseFundamental
    """


class EarningRatios:
    """
    Definition of the EarningRatios class
    """


class FinancialStatements:
    """
    Definition of the FinancialStatements class
    """


class AssetClassification:
    """
    Definition of the AssetClassification class
    """


class EarningReports:
    """
    Definition of the EarningReports class
    """


class CompanyReference:
    """
    Definition of the CompanyReference class
    """


class ValuationRatios:
    """
    Definition of the ValuationRatios class
    """


class CompanyProfile:
    """
    Definition of the CompanyProfile class
    """


class BalanceSheet:
    """
    Definition of the BalanceSheet class
    """


class AmortizationIncomeStatement(MultiPeriodField):
    """
    The non-cash expense recognized on intangible assets over the benefit period of the asset.
    """


class SecuritiesAmortizationIncomeStatement(MultiPeriodField):
    """
    The gradual elimination of a liability, such as a mortgage, in regular payments over a specified period of time. Such payments must
    be sufficient to cover both principal and interest.
    """


class CostOfRevenueIncomeStatement(MultiPeriodField):
    """
    The aggregate cost of goods produced and sold and services rendered during the reporting PeriodAsByte. It excludes all operating
    expenses such as depreciation, depletion, amortization, and SG&amp;A. For the must have cost industry, if the number is not reported
    by the company, it will be calculated based on accounting equation.
    Cost of Revenue = Revenue - Operating Expenses - Operating Profit.
    """


class DepletionIncomeStatement(MultiPeriodField):
    """
    The non-cash expense recognized on natural resources (eg. Oil and mineral deposits) over the benefit period of the asset.
    """


class DepreciationIncomeStatement(MultiPeriodField):
    """
    The current period non-cash expense recognized on tangible assets used in the normal course of business, by allocating the cost of
    assets over their useful lives, in the Income Statement. Examples of tangible asset include buildings, production and equipment.
    """


class DepreciationAndAmortizationIncomeStatement(MultiPeriodField):
    """
    The sum of depreciation and amortization expense in the Income Statement.
    Depreciation is the non-cash expense recognized on tangible assets used in the normal course of business, by allocating the cost of
    assets over their useful lives
    Amortization is the non-cash expense recognized on intangible assets over the benefit period of the asset.
    """


class DepreciationAmortizationDepletionIncomeStatement(MultiPeriodField):
    """
    The sum of depreciation, amortization and depletion expense in the Income Statement.
    Depreciation is the non-cash expense recognized on tangible assets used in the normal course of business, by allocating the cost of
    assets over their useful lives
    Amortization is the non-cash expense recognized on intangible assets over the benefit period of the asset.
    Depletion is the non-cash expense recognized on natural resources (eg. Oil and mineral deposits) over the benefit period of the
    asset.
    """


class NetIncomeDiscontinuousOperationsIncomeStatement(MultiPeriodField):
    """
    To be classified as discontinued operations, if both of the following conditions are met:
    1: The operations and cash flow of the component have been or will be removed from the ongoing operations of the entity as a
    result of the disposal transaction, and
    2: The entity will have no significant continuing involvement in the operations of the component after the disposal transaction.
    The discontinued operation is reported net of tax.
    Gains/Loss on Disposal of Discontinued Operations: Any gains or loss recognized on disposal of discontinued operations,
    which is the difference between the carrying value of the division and its fair value less costs to sell.
    Provision for Gain/Loss on Disposal: The amount of current expense charged in order to prepare for the disposal of
    discontinued operations.
    """


class ExciseTaxesIncomeStatement(MultiPeriodField):
    """
    Excise taxes are taxes paid when purchases are made on a specific good, such as gasoline. Excise taxes are often included in the
    price of the product. There are also excise taxes on activities, such as on wagering or on highway usage by trucks.
    """


class NetIncomeExtraordinaryIncomeStatement(MultiPeriodField):
    """
    Gains (losses), whether arising from extinguishment of debt, prior period adjustments, or from other events or transactions, that are
    both unusual in nature and infrequent in occurrence thereby meeting the criteria for an event or transaction to be classified as an
    extraordinary item.
    """


class FeeRevenueAndOtherIncomeIncomeStatement(MultiPeriodField):
    """
    The aggregate amount of fees, commissions, and other income.
    """


class GeneralAndAdministrativeExpenseIncomeStatement(MultiPeriodField):
    """
    The aggregate total of general managing and administering expenses for the company.
    """


class GrossProfitIncomeStatement(MultiPeriodField):
    """
    Total revenue less cost of revenue. The number is as reported by the company on the income statement; however, the number will
    be calculated if it is not reported. This field is null if the cost of revenue is not given.
    Gross Profit = Total Revenue - Cost of Revenue.
    """


class InterestExpenseIncomeStatement(MultiPeriodField):
    """
    Relates to the general cost of borrowing money. It is the price that a lender charges a borrower for the use of the lender's money.
    """


class InterestExpenseNonOperatingIncomeStatement(MultiPeriodField):
    """
    Interest expense caused by long term financing activities; such as interest expense incurred on trading liabilities, commercial paper,
    long-term debt, capital leases, deposits, and all other borrowings.
    """


class InterestIncomeAfterProvisionForLoanLossIncomeStatement(MultiPeriodField):
    """
    Net interest and dividend income or expense, including any amortization and accretion (as applicable) of discounts and premiums,
    including consideration of the provisions for loan, lease, credit, and other related losses, if any.
    """


class InterestIncomeNonOperatingIncomeStatement(MultiPeriodField):
    """
    Interest income earned from long term financing activities.
    """


class NetNonOperatingInterestIncomeExpenseIncomeStatement(MultiPeriodField):
    """
    Net-Non Operating interest income or expenses caused by financing activities.
    """


class LossAdjustmentExpenseIncomeStatement(MultiPeriodField):
    """
    Losses generally refer to (1) the amount of reduction in the value of an insured's property caused by an insured peril, (2) the amount
    sought through an insured's claim, or (3) the amount paid on behalf of an insured under an insurance contract.  Loss Adjustment
    Expenses is expenses incurred in the course of investigating and settling claims that includes any legal and adjusters' fees and the
    costs of paying claims and all related expenses.
    """


class MinorityInterestsIncomeStatement(MultiPeriodField):
    """
    Represents par or stated value of the subsidiary stock not owned by the parent company plus the minority interest's equity in the
    surplus of the subsidiary. This item includes preferred dividend averages on the minority preferred stock (preferred shares not
    owned by the reporting parent company). Minority interest also refers to stockholders who own less than 50% of a subsidiary's
    outstanding voting common stock. The minority stockholders hold an interest in the subsidiary's net assets and share earnings with
    the parent company.
    """


class NetIncomeIncomeStatement(MultiPeriodField):
    """
    Includes all the operations (continuing and discontinued) and all the other income or charges (extraordinary, accounting changes,
    tax loss carry forward, and other gains and losses).
    """


class NetIncomeCommonStockholdersIncomeStatement(MultiPeriodField):
    """
    Net income minus the preferred dividends paid as presented in the Income Statement.
    """


class NetIncomeContinuousOperationsIncomeStatement(MultiPeriodField):
    """
    Revenue less expenses and taxes from the entity's ongoing operations and before income (loss) from: Preferred Dividends;
    Extraordinary Gains and Losses; Income from Cumulative Effects of Accounting Change; Discontinuing Operation; Income from Tax
    Loss Carry forward; Other Gains/Losses.
    """


class NetInterestIncomeIncomeStatement(MultiPeriodField):
    """
    Total interest income minus total interest expense. It represents the difference between interest and dividends earned on interest-
    bearing assets and interest paid to depositors and other creditors.
    """


class NetInvestmentIncomeIncomeStatement(MultiPeriodField):
    """
    Total of interest, dividends, and other earnings derived from the insurance company's invested assets minus the expenses
    associated with these investments. Excluded from this income are capital gains or losses as the result of the sale of assets, as well
    as any unrealized capital gains or losses.
    """


class TotalRevenueIncomeStatement(MultiPeriodField):
    """
    All sales, business revenues and income that the company makes from its business operations, net of excise taxes. This applies for
    all companies and can be used as comparison for all industries.
    For Normal, Mining, Transportation and Utility templates companies, this is the sum of Operating Revenues, Excise Taxes and Fees.
    For Bank template companies, this is the sum of Net Interest Income and Non-Interest Income.
    For Insurance template companies, this is the sum of Premiums, Interest Income, Fees, Investment and Other Income.
    """


class NonInterestExpenseIncomeStatement(MultiPeriodField):
    """
    Any expenses that not related to interest. It includes labor and related expense, occupancy and equipment, commission,
    professional expense and contract services expenses, selling, general and administrative, research and development depreciation,
    amortization and depletion, and any other special income/charges.
    """


class NonInterestIncomeIncomeStatement(MultiPeriodField):
    """
    The total amount of non-interest income which may be derived from: (1) fees and commissions; (2) premiums earned; (3) equity
    investment; (4) the sale or disposal of assets; and (5) other sources not otherwise specified.
    """


class OperatingExpenseIncomeStatement(MultiPeriodField):
    """
    Operating expenses are primary recurring costs associated with central operations (other than cost of goods sold) that are incurred
    in order to generate sales.
    """


class OperatingIncomeIncomeStatement(MultiPeriodField):
    """
    Income from normal business operations after deducting cost of revenue and operating expenses. It does not include income from
    any investing activities.
    """


class OperatingRevenueIncomeStatement(MultiPeriodField):
    """
    Sales and income that the company makes from its business operations. This applies only to non-bank and insurance companies.
    For Utility template companies, this is the sum of revenue from electric, gas, transportation and other operating revenue.
    For Transportation template companies, this is the sum of revenue-passenger, revenue-cargo, and other operating revenue.
    """


class OtherIncomeExpenseIncomeStatement(MultiPeriodField):
    """
    Income or expense that comes from miscellaneous sources.
    """


class PolicyAcquisitionExpenseIncomeStatement(MultiPeriodField):
    """
    Costs that vary with and are primarily related to the acquisition of new and renewal insurance contracts. Also referred to as
    underwriting expenses.
    """


class NetPolicyholderBenefitsAndClaimsIncomeStatement(MultiPeriodField):
    """
    The net provision in current period for future policy benefits, claims, and claims settlement expenses incurred in the claims
    settlement process before the effects of reinsurance arrangements. The value is net of the effects of contracts assumed and
    ceded.
    """


class PreferredStockDividendsIncomeStatement(MultiPeriodField):
    """
    The amount of dividends declared or paid in the period to preferred shareholders, or the amount for which the obligation to pay
    them dividends arose in the PeriodAsByte. Preferred dividends are the amount required for the current year only, and not for any amount
    required in past years.
    """


class TotalPremiumsEarnedIncomeStatement(MultiPeriodField):
    """
    Premiums earned is the portion of an insurance written premium which is considered "earned" by the insurer, based on the part of
    the policy period that the insurance has been in effect, and during which the insurer has been exposed to loss.
    """


class PretaxIncomeIncomeStatement(MultiPeriodField):
    """
    Reported income before the deduction or benefit of income taxes.
    """


class TaxProvisionIncomeStatement(MultiPeriodField):
    """
    Include any taxes on income, net of any investment tax credits for the current accounting PeriodAsByte.
    """


class CreditLossesProvisionIncomeStatement(MultiPeriodField):
    """
    A charge to income which represents an expense deemed adequate by management given the composition of a bank's credit
    portfolios, their probability of default, the economic environment and the allowance for credit losses already established. Specific
    provisions are established to reduce the book value of specific assets (primarily loans) to establish the amount expected to be
    recovered on the loans.
    """


class ResearchAndDevelopmentIncomeStatement(MultiPeriodField):
    """
    The aggregate amount of research and development expenses during the year.
    """


class SellingAndMarketingExpenseIncomeStatement(MultiPeriodField):
    """
    The aggregate total amount of expenses directly related to the marketing or selling of products or services.
    """


class SellingGeneralAndAdministrationIncomeStatement(MultiPeriodField):
    """
    The aggregate total costs related to selling a firm's product and services, as well as all other general and administrative expenses.
    Selling expenses are those directly related to the company's efforts to generate sales (e.g., sales salaries, commissions,
    advertising, delivery expenses). General and administrative expenses are expenses related to general administration of the
    company's operation (e.g., officers and office salaries, office supplies, telephone, accounting and legal services, and business
    licenses and fees).
    """


class SpecialIncomeChargesIncomeStatement(MultiPeriodField):
    """
    Earnings or losses attributable to occurrences or actions by the firm that is either infrequent or unusual.
    """


class TotalExpensesIncomeStatement(MultiPeriodField):
    """
    The sum of operating expense and cost of revenue. If the company does not give the reported number, it will be calculated by
    adding operating expense and cost of revenue.
    """


class InterestIncomeIncomeStatement(MultiPeriodField):
    """
    Income generated from interest-bearing deposits or accounts.
    """


class EBITIncomeStatement(MultiPeriodField):
    """
    Earnings minus expenses (excluding interest and tax expenses).
    """


class EBITDAIncomeStatement(MultiPeriodField):
    """
    Earnings minus expenses (excluding interest, tax, depreciation, and amortization expenses).
    """


class NetIncomeContinuousOperationsNetMinorityInterestIncomeStatement(MultiPeriodField):
    """
    Revenue less expenses and taxes from the entity's ongoing operations net of minority interest and before income (loss) from:
    Preferred Dividends; Extraordinary Gains and Losses; Income from Cumulative Effects of Accounting Change; Discontinuing
    Operation; Income from Tax Loss Carry forward; Other Gains/Losses.
    """


class CededPremiumsIncomeStatement(MultiPeriodField):
    """
    The amount of premiums paid and payable to another insurer as a result of reinsurance arrangements in order to exchange for that
    company accepting all or part of insurance on a risk or exposure. This item is usually only available for insurance industry.
    """


class CommissionExpensesIncomeStatement(MultiPeriodField):
    """
    
    """


class CreditCardIncomeStatement(MultiPeriodField):
    """
    Income earned from credit card services including late, over limit, and annual fees. This item is usually only available for bank
    industry.
    """


class DividendIncomeIncomeStatement(MultiPeriodField):
    """
    Dividends earned from equity investment securities. This item is usually only available for bank industry.
    """


class EarningsFromEquityInterestIncomeStatement(MultiPeriodField):
    """
    The earnings from equity interest can be a result of any of the following: Income from earnings distribution of the business, either
    as dividends paid to corporate shareholders or as drawings in a partnership; Capital gain realized upon sale of the business; Capital
    gain realized from selling his or her interest to other partners. This item is usually not available for bank and insurance industries.
    """


class EquipmentIncomeStatement(MultiPeriodField):
    """
    Equipment expenses include depreciation, repairs, rentals, and service contract costs. This also includes equipment purchases
    which do not qualify for capitalization in accordance with the entity's accounting policy. This item may also include furniture
    expenses. This item is usually only available for bank industry.
    """


class ExplorationDevelopmentAndMineralPropertyLeaseExpensesIncomeStatement(MultiPeriodField):
    """
    Costs incurred in identifying areas that may warrant examination and in examining specific areas that are considered to have
    prospects of containing energy or metal reserves, including costs of drilling exploratory wells. Development expense is the
    capitalized costs incurred to obtain access to proved reserves and to provide facilities for extracting, treating, gathering and storing
    the energy and metal. Mineral property includes oil and gas wells, mines, and other natural deposits (including geothermal
    deposits). The payment for leasing those properties is called mineral property lease expense. Exploration expense is included in
    operation expenses for mining industry.
    """


class FeesAndCommissionsIncomeStatement(MultiPeriodField):
    """
    Total fees and commissions earned from providing services such as leasing of space or maintaining: (1) depositor accounts; (2)
    transfer agent; (3) fiduciary and trust; (4) brokerage and underwriting; (5) mortgage; (6) credit cards; (7) correspondent clearing;
    and (8) other such services and activities performed for others. This item is usually available for bank and insurance industries.
    """


class ForeignExchangeTradingGainsIncomeStatement(MultiPeriodField):
    """
    Trading revenues that result from foreign exchange exposures such as cash instruments and off-balance sheet derivative
    instruments. This item is usually only available for bank industry.
    """


class FuelIncomeStatement(MultiPeriodField):
    """
    The aggregate amount of fuel cost for current period associated with the revenue generation. This item is usually only available for
    transportation industry.
    """


class FuelAndPurchasePowerIncomeStatement(MultiPeriodField):
    """
    Cost of fuel, purchase power and gas associated with revenue generation. This item is usually only available for utility industry.
    """


class GainOnSaleOfBusinessIncomeStatement(MultiPeriodField):
    """
    The amount of excess earned in comparison to fair value when selling a business. This item is usually not available for insurance
    industry.
    """


class GainOnSaleOfPPEIncomeStatement(MultiPeriodField):
    """
    The amount of excess earned in comparison to the net book value for sale of property, plant, equipment. This item is usually not
    available for bank and insurance industries.
    """


class GainOnSaleOfSecurityIncomeStatement(MultiPeriodField):
    """
    The amount of excess earned in comparison to the original purchase value of the security.
    """


class GrossPremiumsWrittenIncomeStatement(MultiPeriodField):
    """
    Total premiums generated from all policies written by an insurance company within a given period of time. This item is usually only
    available for insurance industry.
    """


class ImpairmentOfCapitalAssetsIncomeStatement(MultiPeriodField):
    """
    Impairments are considered to be permanent, which is a downward revaluation of fixed assets. If the sum of all estimated future
    cash flows is less than the carrying value of the asset, then the asset would be considered impaired and would have to be written
    down to its fair value. Once an asset is written down, it may only be written back up under very few circumstances. Usually the
    company uses the sum of undiscounted future cash flows to determine if the impairment should occur, and uses the sum of
    discounted future cash flows to make the impairment judgment. The impairment decision emphasizes on capital assets' future
    profit collection ability.
    """


class IncreaseDecreaseInNetUnearnedPremiumReservesIncomeStatement(MultiPeriodField):
    """
    Premium might contain a portion of the amount that has been paid in advance for insurance that has not yet been provided, which
    is called unearned premium. If either party cancels the contract, the insurer must have the unearned premium ready to refund.
    Hence, the amount of premium reserve maintained by insurers is called unearned premium reserves, which is prepared for
    liquidation.  This item is usually only available for insurance industry.
    """


class InsuranceAndClaimsIncomeStatement(MultiPeriodField):
    """
    Insurance and claims are the expenses in the period incurred with respect to protection provided by insurance entities against risks
    other than risks associated with production (which is allocated to cost of sales). This item is usually not available for insurance
    industries.
    """


class InterestExpenseForDepositIncomeStatement(MultiPeriodField):
    """
    Includes interest expense on the following deposit accounts: Interest-bearing Demand deposit; Checking account; Savings account;
    Deposit in foreign offices; Money Market Certificates &amp; Deposit Accounts. This item is usually only available for bank industry.
    """


class InterestExpenseForFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement(MultiPeriodField):
    """
    Gross expenses on the purchase of Federal funds at a specified price with a simultaneous agreement to sell the same to the same
    counterparty at a fixed or determinable price at a future date. This item is usually only available for bank industry.
    """


class InterestExpenseForLongTermDebtAndCapitalSecuritiesIncomeStatement(MultiPeriodField):
    """
    The aggregate interest expenses incurred on long-term borrowings and any interest expenses on fixed assets (property, plant,
    equipment) that are leased due longer than one year. This item is usually only available for bank industry.
    """


class InterestExpenseForShortTermDebtIncomeStatement(MultiPeriodField):
    """
    The aggregate interest expenses incurred on short-term borrowings and any interest expenses on fixed assets (property, plant,
    equipment) that are leased within one year. This item is usually only available for bank industry.
    """


class InterestIncomeFromDepositsIncomeStatement(MultiPeriodField):
    """
    Interest income generated from all deposit accounts. This item is usually only available for bank industry.
    """


class InterestIncomeFromFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellIncomeStatement(MultiPeriodField):
    """
    The carrying value of funds outstanding loaned in the form of security resale agreements if the agreement requires the purchaser to
    resell the identical security purchased or a security that meets the definition of ""substantially the same"" in the case of a dollar roll.
    Also includes purchases of participations in pools of securities that are subject to a resale agreement; This category includes all
    interest income generated from federal funds sold and securities purchases under agreements to resell; This category includes all
    interest income generated from federal funds sold and securities purchases under agreements to resell.
    """


class InterestIncomeFromLeasesIncomeStatement(MultiPeriodField):
    """
    Includes interest and fee income generated by direct lease financing. This item is usually only available for bank industry.
    """


class InterestIncomeFromLoansIncomeStatement(MultiPeriodField):
    """
    Loan is a common field to banks. Interest Income from Loans is interest and fee income generated from all loans, which includes
    Commercial loans; Credit loans; Other consumer loans; Real Estate - Construction; Real Estate - Mortgage; Foreign loans. Banks
    earn interest from loans. This item is usually only available for bank industry.
    """


class InterestIncomeFromLoansAndLeaseIncomeStatement(MultiPeriodField):
    """
    Total interest and fee income generated by loans and lease. This item is usually only available for bank industry.
    """


class InterestIncomeFromSecuritiesIncomeStatement(MultiPeriodField):
    """
    Represents total interest and dividend income from U.S. Treasury securities, U.S. government agency and corporation obligations,
    securities issued by states and political subdivisions, other domestic debt securities, foreign debt securities, and equity securities
    (including investments in mutual funds). Excludes interest income from securities held in trading accounts. This item is usually only
    available for bank industry.
    """


class InvestmentBankingProfitIncomeStatement(MultiPeriodField):
    """
    Includes (1) underwriting revenue (the spread between the resale price received and the cost of the securities and related
    expenses) generated through the purchasing, distributing and reselling of new issues of securities (alternatively, could be a
    secondary offering of a large block of previously issued securities); and (2) fees earned for mergers, acquisitions, divestitures,
    restructurings, and other types of financial advisory services. This item is usually only available for bank industry.
    """


class MaintenanceAndRepairsIncomeStatement(MultiPeriodField):
    """
    The aggregate amount of maintenance and repair expenses in the current period associated with the revenue generation. Mainly
    for fixed assets. This item is usually only available for transportation industry.
    """


class NetForeignExchangeGainLossIncomeStatement(MultiPeriodField):
    """
    The aggregate foreign currency translation gain or loss (both realized and unrealized) included as part of revenue. This item is
    usually only available for insurance industry.
    """


class NetOccupancyExpenseIncomeStatement(MultiPeriodField):
    """
    Occupancy expense may include items, such as depreciation of facilities and equipment, lease expenses, property taxes and
    property and casualty insurance expense. This item is usually only available for bank industry.
    """


class NetPremiumsWrittenIncomeStatement(MultiPeriodField):
    """
    Net premiums written are gross premiums written less ceded premiums. This item is usually only available for insurance industry.
    """


class NetRealizedGainLossOnInvestmentsIncomeStatement(MultiPeriodField):
    """
    Gain or loss realized during the period of time for all kinds of investment securities. In might include trading, available-for-sale, or
    held-to-maturity securities. This item is usually only available for insurance industry.
    """


class OccupancyAndEquipmentIncomeStatement(MultiPeriodField):
    """
    Includes total expenses of occupancy and equipment. This item is usually only available for bank industry.
    """


class OperationAndMaintenanceIncomeStatement(MultiPeriodField):
    """
    The aggregate amount of operation and maintenance expenses, which is the one important operating expense for the utility
    industry. It includes any costs related to production and maintenance cost of the property during the revenue generation process.
    This item is usually only available for mining and utility industries.
    """


class OtherCustomerServicesIncomeStatement(MultiPeriodField):
    """
    Represents fees and commissions earned from provide other services. This item is usually only available for bank industry.
    """


class OtherInterestExpenseIncomeStatement(MultiPeriodField):
    """
    All other interest expense that is not otherwise classified
    """


class OtherInterestIncomeIncomeStatement(MultiPeriodField):
    """
    All other interest income that is not otherwise classified
    """


class OtherNonInterestExpenseIncomeStatement(MultiPeriodField):
    """
    All other non interest expense that is not otherwise classified
    """


class OtherSpecialChargesIncomeStatement(MultiPeriodField):
    """
    All other special charges that are not otherwise classified
    """


class OtherTaxesIncomeStatement(MultiPeriodField):
    """
    Any taxes that are not part of income taxes. This item is usually not available for bank and insurance industries.
    """


class PolicyholderBenefitsCededIncomeStatement(MultiPeriodField):
    """
    The provision in current period for future policy benefits, claims, and claims settlement, which is under reinsurance arrangements.
    This item is usually only available for insurance industry.
    """


class PolicyholderBenefitsGrossIncomeStatement(MultiPeriodField):
    """
    The gross amount of provision in current period for future policyholder benefits, claims, and claims settlement, incurred in the
    claims settlement process before the effects of reinsurance arrangements. This item is usually only available for insurance industry.
    """


class PolicyholderDividendsIncomeStatement(MultiPeriodField):
    """
    Payments made or credits extended to the insured by the company, usually at the end of a policy year results in reducing the net
    insurance cost to the policyholder. Such dividends may be paid in cash to the insured or applied by the insured as reductions of the
    premiums due for the next policy year. This item is usually only available for insurance industry.
    """


class PolicyholderInterestIncomeStatement(MultiPeriodField):
    """
    The periodic income payment provided to the annuitant by the insurance company, which is determined by the assumed interest
    rate (AIR) and other factors. This item is usually only available for insurance industry.
    """


class ProfessionalExpenseAndContractServicesExpenseIncomeStatement(MultiPeriodField):
    """
    Professional and contract service expense includes cost reimbursements for support services related to contracted projects,
    outsourced management, technical and staff support. This item is usually only available for bank industry.
    """


class ProvisionForDoubtfulAccountsIncomeStatement(MultiPeriodField):
    """
    Amount of the current period expense charged against operations, the offset which is generally to the allowance for doubtful
    accounts for the purpose of reducing receivables, including notes receivable, to an amount that approximates their net realizable
    value (the amount expected to be collected). The category includes provision for loan losses, provision for any doubtful account
    receivable, and bad debt expenses. This item is usually not available for bank and insurance industries.
    """


class RentAndLandingFeesIncomeStatement(MultiPeriodField):
    """
    Rent fees are the cost of occupying space during the accounting PeriodAsByte. Landing fees are a change paid to an airport company for
    landing at a particular airport. This item is not available for insurance industry.
    """


class RestructuringAndMergernAcquisitionIncomeStatement(MultiPeriodField):
    """
    Expenses are related to restructuring, merger, or acquisitions. Restructuring expenses are charges associated with the
    consolidation and relocation of operations, disposition or abandonment of operations or productive assets. Merger and acquisition
    expenses are the amount of costs of a business combination including legal, accounting, and other costs that were charged to
    expense during the PeriodAsByte.
    """


class SalariesAndWagesIncomeStatement(MultiPeriodField):
    """
    All salary, wages, compensation, management fees, and employee benefit expenses.
    """


class SecuritiesActivitiesIncomeStatement(MultiPeriodField):
    """
    Income/Loss from Securities and Activities
    """


class ServiceChargeOnDepositorAccountsIncomeStatement(MultiPeriodField):
    """
    Includes any service charges on following accounts: Demand Deposit; Checking account; Savings account; Deposit in foreign
    offices; ESCROW accounts; Money Market Certificates &amp; Deposit accounts, CDs (Negotiable Certificates of Deposits); NOW
    Accounts (Negotiable Order of Withdrawal); IRAs (Individual Retirement Accounts). This item is usually only available for bank
    industry.
    """


class TradingGainLossIncomeStatement(MultiPeriodField):
    """
    A broker-dealer or other financial entity may buy and sell securities exclusively for its own account, sometimes referred to as
    proprietary trading. The profit or loss is measured by the difference between the acquisition cost and the selling price or current
    market or fair value. The net gain or loss, includes both realized and unrealized, from trading cash instruments, equities and
    derivative contracts (including commodity contracts) that has been recognized during the accounting period for the broker dealer or
    other financial entity's own account. This item is typically available for bank industry.
    """


class TrustFeesbyCommissionsIncomeStatement(MultiPeriodField):
    """
    Bank manages funds on behalf of its customers through the operation of various trust accounts. Any fees earned through managing
    those funds are called trust fees, which are recognized when earned. This item is typically available for bank industry.
    """


class UnderwritingExpensesIncomeStatement(MultiPeriodField):
    """
    Also known as Policy Acquisition Costs; and reported by insurance companies.  The cost incurred by an insurer when deciding
    whether to accept or decline a risk; may include meetings with the insureds or brokers, actuarial review of loss history, or physical
    inspections of exposures. Also, expenses deducted from insurance company revenues (including incurred losses and acquisition
    costs) to determine underwriting profit.
    """


class WriteOffIncomeStatement(MultiPeriodField):
    """
    A reduction in the value of an asset or earnings by the amount of an expense or loss.
    """


class OtherNonInterestIncomeIncomeStatement(MultiPeriodField):
    """
    Usually available for the banking industry.  This is Non-Interest Income that is not otherwise classified.
    """


class AmortizationOfIntangiblesIncomeStatement(MultiPeriodField):
    """
    The aggregate expense charged against earnings to allocate the cost of intangible assets (nonphysical assets not used in
    production) in a systematic and rational manner to the periods expected to benefit from such assets.
    """


class NetIncomeFromContinuingAndDiscontinuedOperationIncomeStatement(MultiPeriodField):
    """
    Net Income from Continuing Operations and Discontinued Operations, added together.
    """


class NetIncomeFromTaxLossCarryforwardIncomeStatement(MultiPeriodField):
    """
    Occurs if a company has had a net loss from operations on a previous year that can be carried forward to reduce net income for tax
    purposes.
    """


class OtherOperatingExpensesIncomeStatement(MultiPeriodField):
    """
    The aggregate amount of operating expenses associated with normal operations. Will not include any gain, loss, benefit, or income;
    and its value reported by the company should be &lt;0.
    """


class TotalMoneyMarketInvestmentsIncomeStatement(MultiPeriodField):
    """
    The sum of the money market investments held by a bank's depositors, which are FDIC insured.
    """


class ReconciledCostOfRevenueIncomeStatement(MultiPeriodField):
    """
    The Cost Of Revenue plus Depreciation, Depletion &amp; Amortization from the IncomeStatement; minus Depreciation, Depletion &amp;
    Amortization from the Cash Flow Statement
    """


class ReconciledDepreciationIncomeStatement(MultiPeriodField):
    """
    Is Depreciation, Depletion &amp; Amortization from the Cash Flow Statement
    """


class NormalizedIncomeIncomeStatement(MultiPeriodField):
    """
    This calculation represents earnings adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This can be
    used to fairly measure a company's profitability. This is calculated using Net Income from Continuing Operations plus/minus any tax
    affected unusual Items and Goodwill Impairments/Write Offs.
    """


class NetIncomeFromContinuingOperationNetMinorityInterestIncomeStatement(MultiPeriodField):
    """
    Revenue less expenses and taxes from the entity's ongoing operations net of minority interest and before income (loss) from:
    Preferred Dividends; Extraordinary Gains and Losses; Income from Cumulative Effects of Accounting Change; Discontinuing
    Operation; Income from Tax Loss Carry forward; Other Gains/Losses.
    """


class GainLossonSaleofAssetsIncomeStatement(MultiPeriodField):
    """
    Any gain (loss) recognized on the sale of assets or a sale which generates profit or loss, which is a difference between sales price
    and net book value at the disposal time.
    """


class GainonSaleofLoansIncomeStatement(MultiPeriodField):
    """
    Gain on sale of any loans investment.
    """


class GainonSaleofInvestmentPropertyIncomeStatement(MultiPeriodField):
    """
    Gain on the disposal of investment property.
    """


class LossonExtinguishmentofDebtIncomeStatement(MultiPeriodField):
    """
    Loss on extinguishment of debt is the accounting loss that results from a debt extinguishment. A debt shall be accounted for as
    having been extinguished in a number of circumstances, including when it has been settled through repayment or replacement by
    another liability. It generally results in an accounting gain or loss. Amount represents the difference between the fair value of the
    payments made and the carrying amount of the debt at the time of its extinguishment.
    """


class EarningsfromEquityInterestNetOfTaxIncomeStatement(MultiPeriodField):
    """
    Income from other equity interest reported after Provision of Tax. This applies to all industries.
    """


class NetIncomeIncludingNoncontrollingInterestsIncomeStatement(MultiPeriodField):
    """
    Net income of the group after the adjustment of all expenses and benefit.
    """


class OtherunderPreferredStockDividendIncomeStatement(MultiPeriodField):
    """
    Dividend paid to the preferred shareholders before the common stock shareholders.
    """


class StaffCostsIncomeStatement(MultiPeriodField):
    """
    Total staff cost which is paid to the employees that is not part of Selling, General, and Administration expense.
    """


class SocialSecurityCostsIncomeStatement(MultiPeriodField):
    """
    Benefits paid to the employees in respect of their work.
    """


class PensionCostsIncomeStatement(MultiPeriodField):
    """
    The expense that a company incurs each year by providing a pension plan for its employees. Major expenses in the pension cost
    include employer matching contributions and management fees.
    """


class OtherOperatingIncomeTotalIncomeStatement(MultiPeriodField):
    """
    Total Other Operating Income- including interest income, dividend income and other types of operating income.
    """


class IncomefromAssociatesandOtherParticipatingInterestsIncomeStatement(MultiPeriodField):
    """
    Total income from the associates and joint venture via investment, accounted for in the Non-Operating section.
    """


class TotalOtherFinanceCostIncomeStatement(MultiPeriodField):
    """
    Any other finance cost which is not clearly defined in the Non-Operating section.
    """


class GrossDividendPaymentIncomeStatement(MultiPeriodField):
    """
    Total amount paid in dividends to investors- this includes dividends paid on equity and non-equity shares.
    """


class FeesandCommissionIncomeIncomeStatement(MultiPeriodField):
    """
    Fees and commission income earned by bank and insurance companies on the rendering services.
    """


class FeesandCommissionExpenseIncomeStatement(MultiPeriodField):
    """
    Cost incurred by bank and insurance companies for fees and commission income.
    """


class NetTradingIncomeIncomeStatement(MultiPeriodField):
    """
    Any trading income on the securities.
    """


class OtherStaffCostsIncomeStatement(MultiPeriodField):
    """
    Other costs in incurred in lieu of the employees that cannot be identified by other specific items in the Staff Costs section.
    """


class GainonInvestmentPropertiesIncomeStatement(MultiPeriodField):
    """
    Gain on disposal and change in fair value of investment properties.
    """


class AverageDilutionEarningsIncomeStatement(MultiPeriodField):
    """
    Adjustments to reported net income to calculate Diluted EPS, by assuming that all convertible instruments are converted to
    Common Equity. The adjustments usually include the interest expense of debentures when assumed converted and preferred
    dividends of convertible preferred stock when assumed converted.
    """


class GainLossonFinancialInstrumentsDesignatedasCashFlowHedgesIncomeStatement(MultiPeriodField):
    """
    Gain/Loss through hedging activities.
    """


class GainLossonDerecognitionofAvailableForSaleFinancialAssetsIncomeStatement(MultiPeriodField):
    """
    Gain/loss on the write-off of financial assets available-for-sale.
    """


class NegativeGoodwillImmediatelyRecognizedIncomeStatement(MultiPeriodField):
    """
    Negative Goodwill recognized in the Income Statement. Negative Goodwill arises where the net assets at the date of acquisition,
    fairly valued, falls below the cost of acquisition.
    """


class GainsLossesonFinancialInstrumentsDuetoFairValueAdjustmentsinHedgeAccountingTotalIncomeStatement(MultiPeriodField):
    """
    Gain or loss on derivatives investment due to the fair value adjustment.
    """


class ImpairmentLossesReversalsFinancialInstrumentsNetIncomeStatement(MultiPeriodField):
    """
    Impairment or reversal of impairment on financial instrument such as derivative. This is a contra account under Total Revenue in
    banks.
    """


class ClaimsandPaidIncurredIncomeStatement(MultiPeriodField):
    """
    All reported claims arising out of incidents in that year are considered incurred grouped with claims paid out.
    """


class ReinsuranceRecoveriesClaimsandBenefitsIncomeStatement(MultiPeriodField):
    """
    Claim on the reinsurance company and take the benefits.
    """


class ChangeinInsuranceLiabilitiesNetofReinsuranceIncomeStatement(MultiPeriodField):
    """
    Income/Expense due to changes between periods in insurance liabilities.
    """


class ChangeinInvestmentContractIncomeStatement(MultiPeriodField):
    """
    Income/Expense due to changes between periods in Investment Contracts.
    """


class CreditRiskProvisionsIncomeStatement(MultiPeriodField):
    """
    Provision for the risk of loss of principal or loss of a financial reward stemming from a borrower's failure to repay a loan or otherwise
    meet a contractual obligation. Credit risk arises whenever a borrower is expecting to use future cash flows to pay a current debt.
    Investors are compensated for assuming credit risk by way of interest payments from the borrower or issuer of a debt obligation.
    This is a contra account under Total Revenue in banks.
    """


class WagesandSalariesIncomeStatement(MultiPeriodField):
    """
    This is the portion under Staff Costs that represents salary paid to the employees in respect of their work.
    """


class OtherNonOperatingIncomeExpensesIncomeStatement(MultiPeriodField):
    """
    Total other income and expense of the company that cannot be identified by other specific items in the Non-Operating section.
    """


class OtherNonOperatingIncomeIncomeStatement(MultiPeriodField):
    """
    Other income of the company that cannot be identified by other specific items in the Non-Operating section.
    """


class OtherNonOperatingExpensesIncomeStatement(MultiPeriodField):
    """
    Other expenses of the company that cannot be identified by other specific items in the Non-Operating section.
    """


class TotalUnusualItemsIncomeStatement(MultiPeriodField):
    """
    Total unusual items including Negative Goodwill.
    """


class TotalUnusualItemsExcludingGoodwillIncomeStatement(MultiPeriodField):
    """
    The sum of all the identifiable operating and non-operating unusual items.
    """


class TaxRateForCalcsIncomeStatement(MultiPeriodField):
    """
    Tax rate used for Morningstar calculations.
    """


class TaxEffectOfUnusualItemsIncomeStatement(MultiPeriodField):
    """
    Tax effect of the usual items
    """


class NormalizedEBITDAIncomeStatement(MultiPeriodField):
    """
    EBITDA less Total Unusual Items
    """


class StockBasedCompensationIncomeStatement(MultiPeriodField):
    """
    The cost to the company for granting stock options to reward employees.
    """


class DilutedNIAvailtoComStockholdersIncomeStatement(MultiPeriodField):
    """
    Net income to calculate Diluted EPS, accounting for adjustments assuming that all the convertible instruments are being converted
    to Common Equity.
    """


class InvestmentContractLiabilitiesIncurredIncomeStatement(MultiPeriodField):
    """
    Income/Expenses due to the insurer's liabilities incurred in Investment Contracts.
    """


class ReinsuranceRecoveriesofInvestmentContractIncomeStatement(MultiPeriodField):
    """
    Income/Expense due to recoveries from reinsurers for Investment Contracts.
    """


class TotalDividendPaymentofEquitySharesIncomeStatement(MultiPeriodField):
    """
    Total amount paid in dividends to equity securities investors.
    """


class TotalDividendPaymentofNonEquitySharesIncomeStatement(MultiPeriodField):
    """
    Total amount paid in dividends to Non-Equity securities investors.
    """


class ChangeinTheGrossProvisionforUnearnedPremiumsIncomeStatement(MultiPeriodField):
    """
    The change in the amount of the unearned premium reserves maintained by insurers.
    """


class ChangeinTheGrossProvisionforUnearnedPremiumsReinsurersShareIncomeStatement(MultiPeriodField):
    """
    The change in the amount of unearned premium reserve to be covered by reinsurers.
    """


class ClaimsandChangeinInsuranceLiabilitiesIncomeStatement(MultiPeriodField):
    """
    Income/Expense due to the insurer's changes in insurance liabilities.
    """


class ReinsuranceRecoveriesofInsuranceLiabilitiesIncomeStatement(MultiPeriodField):
    """
    Income/Expense due to recoveries from reinsurers for insurance liabilities.
    """


class TotalOperatingIncomeAsReportedIncomeStatement(MultiPeriodField):
    """
    Operating profit/loss as reported by the company, may be the same or not the same as Morningstar's standardized definition.
    """


class OtherGAIncomeStatement(MultiPeriodField):
    """
    Other General and Administrative Expenses not categorized that the company incurs that are not directly tied to a specific function
    such as manufacturing, production, or sales.
    """


class OtherCostofRevenueIncomeStatement(MultiPeriodField):
    """
    Other costs associated with the revenue-generating activities of the company not categorized above.
    """


class RentandLandingFeesCostofRevenueIncomeStatement(MultiPeriodField):
    """
    Costs paid to use the facilities necessary to generate revenue during the accounting PeriodAsByte.
    """


class DDACostofRevenueIncomeStatement(MultiPeriodField):
    """
    Costs of depreciation and amortization on assets used for the revenue-generating activities during the accounting period
    """


class RentExpenseSupplementalIncomeStatement(MultiPeriodField):
    """
    The sum of all rent expenses incurred by the company for operating leases during the year, it is a supplemental value which would
    be reported outside consolidated statements or consolidated statement's footnotes.
    """


class NormalizedPreTaxIncomeIncomeStatement(MultiPeriodField):
    """
    This calculation represents pre-tax earnings adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This
    can be used to fairly measure a company's profitability. This is calculated using Pre-Tax Income plus/minus any unusual Items and
    Goodwill Impairments/Write Offs.
    """


class ResearchAndDevelopmentExpensesSupplementalIncomeStatement(MultiPeriodField):
    """
    The aggregate amount of research and development expenses during the year. It is a supplemental value which would be reported
    outside consolidated statements.
    """


class DepreciationSupplementalIncomeStatement(MultiPeriodField):
    """
    The current period expense charged against earnings on tangible asset over its useful life. It is a supplemental value which would
    be reported outside consolidated statements.
    """


class AmortizationSupplementalIncomeStatement(MultiPeriodField):
    """
    The current period expense charged against earnings on intangible asset over its useful life. It is a supplemental value which would
    be reported outside consolidated statements.
    """


class TotalRevenueAsReportedIncomeStatement(MultiPeriodField):
    """
    Total revenue as reported by the company, may be the same or not the same as Morningstar's standardized definition.
    """


class OperatingExpenseAsReportedIncomeStatement(MultiPeriodField):
    """
    Operating expense as reported by the company, may be the same or not the same as Morningstar's standardized definition.
    """


class NormalizedIncomeAsReportedIncomeStatement(MultiPeriodField):
    """
    Earnings adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This can be used to fairly measure a
    company's profitability. This is as reported by the company, may be the same or not the same as Morningstar's standardized
    definition.
    """


class NormalizedEBITDAAsReportedIncomeStatement(MultiPeriodField):
    """
    EBITDA less Total Unusual Items. This is as reported by the company, may be the same or not the same as Morningstar's
    standardized definition.
    """


class NormalizedEBITAsReportedIncomeStatement(MultiPeriodField):
    """
    EBIT less Total Unusual Items. This is as reported by the company, may be the same or not the same as Morningstar's standardized
    definition.
    """


class NormalizedOperatingProfitAsReportedIncomeStatement(MultiPeriodField):
    """
    Operating profit adjusted for items that are irregular or unusual in nature, and/or are non-recurring. This can be used to fairly
    measure a company's profitability. This is as reported by the company, may be the same or not the same as Morningstar's
    standardized definition.
    """


class EffectiveTaxRateAsReportedIncomeStatement(MultiPeriodField):
    """
    The average tax rate for the period as reported by the company, may be the same or not the same as Morningstar's standardized
    definition.
    """


class AccountsPayableBalanceSheet(MultiPeriodField):
    """
    Any money that a company owes its suppliers for goods and services purchased on credit and is expected to pay within the next
    year or operating cycle.
    """


class AccountsReceivableBalanceSheet(MultiPeriodField):
    """
    Accounts owed to a company by customers within a year as a result of exchanging goods or services on credit.
    """


class CurrentAccruedExpensesBalanceSheet(MultiPeriodField):
    """
    An expense recognized before it is paid for. Includes compensation, interest, pensions and all other miscellaneous accruals
    reported by the company. Expenses incurred during the accounting period, but not required to be paid until a later date.
    """


class NonCurrentAccruedExpensesBalanceSheet(MultiPeriodField):
    """
    An expense that has occurred but the transaction has not been entered in the accounting records. Accordingly, an adjusting entry
    is made to debit the appropriate expense account and to credit a liability account such as accrued expenses payable or accounts
    payable.
    """


class AccruedInvestmentIncomeBalanceSheet(MultiPeriodField):
    """
    Interest, dividends, rents, ancillary and other revenues earned but not yet received by the entity on its investments.
    """


class AccumulatedDepreciationBalanceSheet(MultiPeriodField):
    """
    The cumulative amount of wear and tear or obsolescence charged against the fixed assets of a company.
    """


class GainsLossesNotAffectingRetainedEarningsBalanceSheet(MultiPeriodField):
    """
    The aggregate amount of gains or losses that are not part of retained earnings. It is also called other comprehensive income.
    """


class AdditionalPaidInCapitalBalanceSheet(MultiPeriodField):
    """
    Excess of issue price over par or stated value of the entity's capital stock and amounts received from other transactions involving
    the entity's stock or stockholders. Includes adjustments to additional paid in capital. There are two major categories of additional
    paid in capital: 1) Paid in capital in excess of par/stated value, which is the difference between the actual issue price of the shares
    and the shares' par/stated value. 2) Paid in capital from other transactions which includes treasury stock, retirement of stock, stock
    dividends recorded at market, lapse of stock purchase warrants, conversion of convertible bonds in excess of the par value of the
    stock, and any other additional capital from the company's own stock transactions.
    """


class AllowanceForLoansAndLeaseLossesBalanceSheet(MultiPeriodField):
    """
    A contra account sets aside as an allowance for bad loans (e.g. customer defaults).
    """


class AvailableForSaleSecuritiesBalanceSheet(MultiPeriodField):
    """
    For an unclassified balance sheet, this item represents equity securities categorized neither as held-to-maturity nor trading. Equity
    securities represent ownership interests or the right to acquire ownership interests in corporations and other legal entities which
    ownership interest is represented by shares of common or preferred stock (which is not mandatory redeemable or redeemable at
    the option of the holder), convertible securities, stock rights, or stock warrants. This category includes preferred stocks, available-
    for-sale and common stock, available-for-sale.
    """


class CapitalStockBalanceSheet(MultiPeriodField):
    """
    The total amount of stock authorized for issue by a corporation, including common and preferred stock.
    """


class CashBalanceSheet(MultiPeriodField):
    """
    Cash includes currency on hand as well as demand deposits with banks or financial institutions. It also includes other kinds of
    accounts that have the general characteristics of demand deposits in that the customer may deposit additional funds at any time
    and also effectively may withdraw funds at any time without prior notice or penalty.
    """


class CashEquivalentsBalanceSheet(MultiPeriodField):
    """
    Cash equivalents, excluding items classified as marketable securities, include short-term, highly liquid investments that are both
    readily convertible to known amounts of cash, and so near their maturity that they present insignificant risk of changes in value
    because of changes in interest rates.  Generally, only investments with original maturities of three months or less qualify under this
    definition. Original maturity means original maturity to the entity holding the investment. For example, both a three-month US
    Treasury bill and a three-year Treasury note purchased three months from maturity qualify as cash equivalents. However, a Treasury
    note purchased three years ago does not become a cash equivalent when its remaining maturity is three months.
    """


class CashAndCashEquivalentsBalanceSheet(MultiPeriodField):
    """
    Includes unrestricted cash on hand, money market instruments and other debt securities which can be converted to cash
    immediately.
    """


class CashAndDueFromBanksBalanceSheet(MultiPeriodField):
    """
    Includes cash on hand (currency and coin), cash items in process of collection, non-interest bearing deposits due from other
    financial institutions (including corporate credit unions), and balances with the Federal Reserve Banks, Federal Home Loan Banks
    and central banks.
    """


class CashCashEquivalentsAndFederalFundsSoldBalanceSheet(MultiPeriodField):
    """
    The aggregate amount of cash, cash equivalents, and federal funds sold.
    """


class CashCashEquivalentsAndMarketableSecuritiesBalanceSheet(MultiPeriodField):
    """
    The aggregate amount of cash, cash equivalents, and marketable securities.
    """


class CommonStockBalanceSheet(MultiPeriodField):
    """
    Common stock (all issues) at par value, as reported within the Stockholder's Equity section of the balance sheet; i.e. it is one
    component of Common Stockholder's Equity
    """


class CurrentAssetsBalanceSheet(MultiPeriodField):
    """
    The total amount of assets considered to be convertible into cash within a relatively short period of time, usually a year.
    """


class CurrentDebtBalanceSheet(MultiPeriodField):
    """
    Represents the total amount of long-term debt such as bank loans and commercial paper, which is due within one year.
    """


class CurrentDebtAndCapitalLeaseObligationBalanceSheet(MultiPeriodField):
    """
    All borrowings due within one year including current portions of long-term debt and capital leases as well as short-term debt such
    as bank loans and commercial paper.
    """


class CurrentLiabilitiesBalanceSheet(MultiPeriodField):
    """
    The debts or obligations of the firm that are due within one year.
    """


class CurrentCapitalLeaseObligationBalanceSheet(MultiPeriodField):
    """
    Represents the total amount of long-term capital leases that must be paid within the next accounting PeriodAsByte. Capital lease
    obligations are contractual obligations that arise from obtaining the use of property or equipment via a capital lease contract.
    """


class DeferredAssetsBalanceSheet(MultiPeriodField):
    """
    An amount owed to a firm that is not expected to be received by the firm within one year from the date of the balance sheet.
    """


class DeferredCostsBalanceSheet(MultiPeriodField):
    """
    An expenditure not recognized as a cost of operation of the period in which incurred, but carried forward to be written off in future
    periods.
    """


class NonCurrentDeferredLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Represents the non-current portion of obligations, which is a liability that usually would have been paid but is now past due.
    """


class CurrentDeferredLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Represents the current portion of obligations, which is a liability that usually would have been paid but is now past due.
    """


class DeferredPolicyAcquisitionCostsBalanceSheet(MultiPeriodField):
    """
    Net amount of deferred policy acquisition costs capitalized on contracts remaining in force as of the balance sheet date.
    """


class CurrentDeferredRevenueBalanceSheet(MultiPeriodField):
    """
    Represents collections of cash or other assets related to revenue producing activity for which revenue has not yet been recognized.
    Generally, an entity records deferred revenue when it receives consideration from a customer before achieving certain criteria that
    must be met for revenue to be recognized in conformity with GAAP. It can be either current or non-current item. Also called
    unearned revenue.
    """


class NonCurrentDeferredRevenueBalanceSheet(MultiPeriodField):
    """
    The non-current portion of deferred revenue amount as of the balance sheet date. Deferred revenue is a liability related to revenue
    producing activity for which revenue has not yet been recognized, and is not expected be recognized in the next twelve months.
    """


class DeferredTaxAssetsBalanceSheet(MultiPeriodField):
    """
    An asset on a company's balance sheet that may be used to reduce any subsequent period's income tax expense. Deferred tax
    assets can arise due to net loss carryovers, which are only recorded as assets if it is deemed more likely than not that the asset
    will be used in future fiscal periods.
    """


class CurrentDeferredTaxesAssetsBalanceSheet(MultiPeriodField):
    """
    Meaning a future tax asset, resulting from temporary differences between book (accounting) value of assets and liabilities and their
    tax value, or timing differences between the recognition of gains and losses in financial statements and their recognition in a tax
    computation. It is also called future tax.
    """


class CurrentDeferredTaxesLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Meaning a future tax liability, resulting from temporary differences between book (accounting) value of assets and liabilities and
    their tax value, or timing differences between the recognition of gains and losses in financial statements and their recognition in a
    tax computation. Deferred tax liabilities generally arise where tax relief is provided in advance of an accounting expense, or income
    is accrued but not taxed until received.
    """


class NonCurrentDeferredTaxesAssetsBalanceSheet(MultiPeriodField):
    """
    A result of timing differences between taxable incomes reported on the income statement and taxable income from the company's
    tax return. Depending on the positioning of deferred income taxes, the field may be either current (within current assets) or non-
    current (below total current assets). Typically a company will have two deferred income taxes fields.
    """


class NonCurrentDeferredTaxesLiabilitiesBalanceSheet(MultiPeriodField):
    """
    The estimated future tax obligations, which usually arise when different accounting methods are used for financial statements and
    tax statement It is also an add-back to the cash flow statement. Deferred income taxes include accumulated tax deferrals due to
    accelerated depreciation and investment credit.
    """


class EquityInvestmentsBalanceSheet(MultiPeriodField):
    """
    This asset represents equity securities categorized neither as held-to-maturity nor trading.
    """


class FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchaseBalanceSheet(MultiPeriodField):
    """
    This liability refers to the amount shown on the books that a bank with insufficient reserves borrows, at the federal funds rate, from
    another bank to meet its reserve requirements; and the amount of securities that an institution sells and agrees to repurchase at a
    specified date for a specified price, net of any reductions or offsets.
    """


class FederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResellBalanceSheet(MultiPeriodField):
    """
    This asset refers to very-short-term loans of funds to other banks and securities dealers.
    """


class FixedMaturityInvestmentsBalanceSheet(MultiPeriodField):
    """
    This asset refers to types of investments that may be contained within the fixed maturity category which securities are having a
    stated final repayment date. Examples of items within this category may include bonds, including convertibles and bonds with
    warrants, and redeemable preferred stocks.
    """


class FuturePolicyBenefitsBalanceSheet(MultiPeriodField):
    """
    Accounting policy pertaining to an insurance entity's net liability for future benefits (for example, death, cash surrender value) to be
    paid to or on behalf of policyholders, describing the bases, methodologies and components of the reserve, and assumptions
    regarding estimates of expected investment yields, mortality, morbidity, terminations and expenses.
    """


class GeneralPartnershipCapitalBalanceSheet(MultiPeriodField):
    """
    In a limited partnership or master limited partnership form of business, this represents the balance of capital held by the general
    partners.
    """


class GoodwillBalanceSheet(MultiPeriodField):
    """
    The excess of the cost of an acquired company over the sum of the fair market value of its identifiable individual assets less the
    liabilities.
    """


class GoodwillAndOtherIntangibleAssetsBalanceSheet(MultiPeriodField):
    """
    Rights or economic benefits, such as patents and goodwill, that is not physical in nature. They are those that are neither physical
    nor financial in nature, nevertheless, have value to the company. Intangibles are listed net of accumulated amortization.
    """


class GrossLoanBalanceSheet(MultiPeriodField):
    """
    Represents the sum of all loans (commercial, consumer, mortgage, etc.) as well as leases before any provisions for loan losses or
    unearned discounts.
    """


class GrossPPEBalanceSheet(MultiPeriodField):
    """
    Carrying amount at the balance sheet date for long-lived physical assets used in the normal conduct of business and not intended
    for resale. This can include land, physical structures, machinery, vehicles, furniture, computer equipment, construction in progress,
    and similar items. Amount does not include depreciation.
    """


class HeldToMaturitySecuritiesBalanceSheet(MultiPeriodField):
    """
    Debt securities that a firm has the ability and intent to hold until maturity.
    """


class IncomeTaxPayableBalanceSheet(MultiPeriodField):
    """
    A current liability account which reflects the amount of income taxes currently due to the federal, state, and local governments.
    """


class InterestBearingDepositsLiabilitiesBalanceSheet(MultiPeriodField):
    """
    The aggregate of all domestic and foreign deposits in the bank that earns interests.
    """


class InterestPayableBalanceSheet(MultiPeriodField):
    """
    Sum of the carrying values as of the balance sheet date of interest payable on all forms of debt, including trade payable that has
    been incurred.
    """


class InterestBearingDepositsAssetsBalanceSheet(MultiPeriodField):
    """
    Deposit of money with a financial institution, in consideration of which the financial institution pays or credits interest, or amounts in the nature
    of interest.
    """


class InventoryBalanceSheet(MultiPeriodField):
    """
    A company's merchandise, raw materials, and finished and unfinished products which have not yet been sold.
    """


class InvestmentsAndAdvancesBalanceSheet(MultiPeriodField):
    """
    All investments in affiliates, real estate, securities, etc. Non-current investment, not including marketable securities.
    """


class LimitedPartnershipCapitalBalanceSheet(MultiPeriodField):
    """
    In a limited partnership or master limited partnership form of business, this represents the balance of capital held by the limited
    partners.
    """


class LongTermDebtBalanceSheet(MultiPeriodField):
    """
    Sum of the carrying values as of the balance sheet date of all long-term debt, which is debt initially having maturities due after one
    year or beyond the operating cycle, if longer, but excluding the portions thereof scheduled to be repaid within one year or the
    normal operating cycle, if longer. Long-term debt includes notes payable, bonds payable, mortgage loans, convertible debt,
    subordinated debt and other types of long term debt.
    """


class LongTermDebtAndCapitalLeaseObligationBalanceSheet(MultiPeriodField):
    """
    All borrowings lasting over one year including long-term debt and long-term portion of capital lease obligations.
    """


class LongTermInvestmentsBalanceSheet(MultiPeriodField):
    """
    Often referred to simply as "investments". Long-term investments are to be held for many years and are not intended to be
    disposed in the near future. This group usually consists of four types of investments.
    """


class LongTermCapitalLeaseObligationBalanceSheet(MultiPeriodField):
    """
    Represents the total liability for long-term leases lasting over one year. Amount equal to the present value (the principal) at the
    beginning of the lease term less lease payments during the lease term.
    """


class MinorityInterestBalanceSheet(MultiPeriodField):
    """
    Carrying amount of the equity interests owned by non-controlling shareholders, partners, or other equity holders in one or more of
    the entities included in the reporting entity's consolidated financial statements.
    """


class MoneyMarketInvestmentsBalanceSheet(MultiPeriodField):
    """
    Short-term (typical maturity is less than one year), highly liquid government or corporate debt instrument such as bankers'
    acceptance, promissory notes, and treasury bills.
    """


class NetLoanBalanceSheet(MultiPeriodField):
    """
    Represents the value of all loans after deduction of the appropriate allowances for loan and lease losses.
    """


class NetPPEBalanceSheet(MultiPeriodField):
    """
    Tangible assets that are held by an entity for use in the production or supply of goods and services, for rental to others, or for
    administrative purposes and that are expected to provide economic benefit for more than one year; net of accumulated
    depreciation.
    """


class NonInterestBearingDepositsBalanceSheet(MultiPeriodField):
    """
    The aggregate amount of all domestic and foreign deposits in the banks that do not draw interest.
    """


class CurrentNotesPayableBalanceSheet(MultiPeriodField):
    """
    Written promises to pay a stated sum at one or more specified dates in the future, within the accounting PeriodAsByte.
    """


class NotesReceivableBalanceSheet(MultiPeriodField):
    """
    An amount representing an agreement for an unconditional promise by the maker to pay the entity (holder) a definite sum of money
    at a future date(s) within one year of the balance sheet date or the normal operating cycle, whichever is longer. Such amount may
    include accrued interest receivable in accordance with the terms of the note. The note also may contain provisions including a
    discount or premium, payable on demand, secured, or unsecured, interest bearing or non-interest bearing, among a myriad of other
    features and characteristics.
    """


class NonCurrentNoteReceivablesBalanceSheet(MultiPeriodField):
    """
    An amount representing an agreement for an unconditional promise by the maker to pay the entity (holder) a definite sum of money
    at a future date(s), excluding the portion that is expected to be received within one year of the balance sheet date or the normal
    operating cycle, whichever is longer.
    """


class OtherCurrentLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Other current liabilities = Total current liabilities - Payables and accrued Expenses - Current debt and capital lease obligation -
    provisions, current - deferred liabilities, current.
    """


class OtherIntangibleAssetsBalanceSheet(MultiPeriodField):
    """
    Sum of the carrying amounts of all intangible assets, excluding goodwill.
    """


class OtherShortTermInvestmentsBalanceSheet(MultiPeriodField):
    """
    The aggregate amount of short term investments, which will be expired within one year that are not specifically classified as
    Available-for-Sale, Held-to-Maturity,  nor Trading investments.
    """


class PayablesBalanceSheet(MultiPeriodField):
    """
    The sum of all payables owed and expected to be paid within one year or one operating cycle, including accounts payables, taxes
    payable, dividends payable and all other current payables.
    """


class PayablesAndAccruedExpensesBalanceSheet(MultiPeriodField):
    """
    This balance sheet account includes all current payables and accrued expenses.
    """


class PolicyReservesBenefitsBalanceSheet(MultiPeriodField):
    """
    Accounting policy pertaining to an insurance entity's net liability for future benefits (for example, death, cash surrender value) to be
    paid to or on behalf of policyholders, describing the bases, methodologies and components of the reserve, and assumptions
    regarding estimates of expected investment yields, mortality, morbidity, terminations and expenses.
    """


class PolicyholderFundsBalanceSheet(MultiPeriodField):
    """
    The total liability as of the balance sheet date of amounts due to policy holders, excluding future policy benefits and claims,
    including unpaid policy dividends, retrospective refunds, and undistributed earnings on participating business.
    """


class PreferredSecuritiesOutsideStockEquityBalanceSheet(MultiPeriodField):
    """
    Preferred securities that that firm treats as a liability. It includes convertible preferred stock or redeemable preferred stock.
    """


class PreferredStockBalanceSheet(MultiPeriodField):
    """
    Preferred stock (all issues) at par value, as reported within the Stockholder's Equity section of the balance sheet.
    """


class PrepaidAssetsBalanceSheet(MultiPeriodField):
    """
    Sum of the carrying amounts that are paid in advance for expenses, which will be charged against earnings in subsequent periods.
    """


class NonCurrentPrepaidAssetsBalanceSheet(MultiPeriodField):
    """
    Sum of the carrying amounts that are paid in advance for expenses, which will be charged against earnings in periods after one
    year or beyond the operating cycle, if longer.
    """


class ReceivablesBalanceSheet(MultiPeriodField):
    """
    The sum of all receivables owed by customers and affiliates within one year, including accounts receivable, notes receivable,
    premiums receivable, and other current receivables.
    """


class ReinsuranceRecoverableBalanceSheet(MultiPeriodField):
    """
    The amount of benefits the ceding insurer expects to recover on insurance policies ceded to other insurance entities as of the
    balance sheet date for all guaranteed benefit types. It includes estimated amounts for claims incurred but not reported, and policy
    benefits, net of any related valuation allowance.
    """


class RetainedEarningsBalanceSheet(MultiPeriodField):
    """
    The cumulative net income of the company from the date of its inception (or reorganization) to the date of the financial statement
    less the cumulative distributions to shareholders either directly (dividends) or indirectly (treasury stock).
    """


class SecuritiesLendingCollateralBalanceSheet(MultiPeriodField):
    """
    The carrying value as of the balance sheet date of the liabilities collateral securities loaned to other broker-dealers. Borrowers of
    securities generally are required to provide collateral to the lenders of securities, commonly cash but sometimes other securities or
    standby letters of credit, with a value slightly higher than that of the securities borrowed.
    """


class SecurityAgreeToBeResellBalanceSheet(MultiPeriodField):
    """
    The carrying value of funds outstanding loaned in the form of security resale agreements if the agreement requires the purchaser to
    resell the identical security purchased or a security that meets the definition of "substantially the same" in the case of a dollar roll.
    Also includes purchases of participations in pools of securities that are subject to a resale agreement.
    """


class SecuritySoldNotYetRepurchasedBalanceSheet(MultiPeriodField):
    """
    Represent obligations of the company to deliver the specified security at the contracted price and, thereby, create a liability to
    purchase the security in the market at prevailing prices.
    """


class SeparateAccountAssetsBalanceSheet(MultiPeriodField):
    """
    The fair value of the assets held by the company for the benefit of separate account policyholders.
    """


class SeparateAccountBusinessBalanceSheet(MultiPeriodField):
    """
    Refers to revenue that is generated that is not part of typical operations.
    """


class ShortTermInvestmentsAvailableForSaleBalanceSheet(MultiPeriodField):
    """
    The current assets section of a company's balance sheet that contains the investments that a company holds with the purpose for
    trading.
    """


class ShortTermInvestmentsHeldToMaturityBalanceSheet(MultiPeriodField):
    """
    The current assets section of a company's balance sheet that contains the investments that a company has made that will expire
    at a fixed date within one year.
    """


class ShortTermInvestmentsTradingBalanceSheet(MultiPeriodField):
    """
    The current assets section of a company's balance sheet that contains the investments that a company can trade at any moment.
    """


class StockholdersEquityBalanceSheet(MultiPeriodField):
    """
    The residual interest in the assets of the enterprise that remains after deducting its liabilities. Equity is increased by owners'
    investments and by comprehensive income, and it is reduced by distributions to the owners.
    """


class TotalTaxPayableBalanceSheet(MultiPeriodField):
    """
    A liability that reflects the taxes owed to federal, state, and local tax authorities. It is the carrying value as of the balance sheet
    date of obligations incurred and payable for statutory income, sales, use, payroll, excise, real, property and other taxes.
    """


class TotalAssetsBalanceSheet(MultiPeriodField):
    """
    The aggregate amount of probable future economic benefits obtained or controlled by a particular enterprise as a result of past
    transactions or events.
    """


class TotalDepositsBalanceSheet(MultiPeriodField):
    """
    A liability account which represents the total amount of funds deposited.
    """


class TotalInvestmentsBalanceSheet(MultiPeriodField):
    """
    Asset that refers to the sum of all available for sale securities and other investments often reported on the balance sheet of
    insurance firms.
    """


class TotalNonCurrentAssetsBalanceSheet(MultiPeriodField):
    """
    Sum of the carrying amounts as of the balance sheet date of all assets that are expected to be realized in cash, sold or consumed
    after one year or beyond the normal operating cycle, if longer.
    """


class TotalPartnershipCapitalBalanceSheet(MultiPeriodField):
    """
    Ownership interest of different classes of partners in the publicly listed limited partnership or master limited partnership. Partners
    include general, limited and preferred partners.
    """


class TradingAssetsBalanceSheet(MultiPeriodField):
    """
    Trading account assets are bought and held principally for the purpose of selling them in the near term (thus held for only a short
    period of time). Unrealized holding gains and losses for trading securities are included in earnings.
    """


class TradingLiabilitiesBalanceSheet(MultiPeriodField):
    """
    The carrying amount of liabilities as of the balance sheet date that pertain to principal and customer trading transactions, or which
    may be incurred with the objective of generating a profit from short-term fluctuations in price as part of an entity's market-making,
    hedging and proprietary trading. Examples include short positions in securities, derivatives and commodities, obligations under
    repurchase agreements, and securities borrowed arrangements.
    """


class TradingSecuritiesBalanceSheet(MultiPeriodField):
    """
    The total of financial instruments that are bought and held principally for the purpose of selling them in the near term (thus held for
    only a short period of time) or for debt and equity securities formerly categorized as available-for-sale or held-to-maturity which the
    company held as of the date it opted to account for such securities at fair value.
    """


class TreasuryStockBalanceSheet(MultiPeriodField):
    """
    The portion of shares that a company keeps in their own treasury. Treasury stock may have come from a repurchase or buyback
    from shareholders; or it may have never been issued to the public in the first place. These shares don't pay dividends, have no
    voting rights, and are not included in shares outstanding calculations.
    """


class UnearnedIncomeBalanceSheet(MultiPeriodField):
    """
    Income received but not yet earned, it represents the unearned amount that is netted against the total loan.
    """


class UnearnedPremiumsBalanceSheet(MultiPeriodField):
    """
    Carrying amount of premiums written on insurance contracts that have not been earned as of the balance sheet date.
    """


class UnpaidLossAndLossReserveBalanceSheet(MultiPeriodField):
    """
    Liability amount that reflects claims that are expected based upon statistical projections, but which have not been reported to the
    insurer.
    """


class InvestedCapitalBalanceSheet(MultiPeriodField):
    """
    Invested capital = common shareholders' equity + long term debt + current debt
    """


class CurrentDeferredAssetsBalanceSheet(MultiPeriodField):
    """
    Payments that will be assigned as expenses with one accounting period, but that are paid in advance and temporarily set up as
    current assets on the balance sheet.
    """


class NonCurrentDeferredAssetsBalanceSheet(MultiPeriodField):
    """
    Payments that will be assigned as expenses longer than one accounting period, but that are paid in advance and temporarily set up
    as non-current assets on the balance sheet.
    """


class SecuritiesAndInvestmentsBalanceSheet(MultiPeriodField):
    """
    Asset, often applicable to Banks, which refers to the aggregate amount of all securities and investments.
    """


class TotalLiabilitiesNetMinorityInterestBalanceSheet(MultiPeriodField):
    """
    Probable future sacrifices of economic benefits arising from present obligations of an enterprise to transfer assets or provide
    services to others in the future as a result of past transactions or events, excluding minority interest.
    """


class TotalNonCurrentLiabilitiesNetMinorityInterestBalanceSheet(MultiPeriodField):
    """
    Total obligations, net minority interest, incurred as part of normal operations that is expected to be repaid beyond the following
    twelve months or one business cycle; excludes minority interest.
    """


class TotalEquityGrossMinorityInterestBalanceSheet(MultiPeriodField):
    """
    Residual interest, including minority interest, that remains in the assets of the enterprise after deducting its liabilities. Equity is
    increased by owners' investments and by comprehensive income, and it is reduced by distributions to the owners.
    """


class GrossAccountsReceivableBalanceSheet(MultiPeriodField):
    """
    Accounts owed to a company by customers within a year as a result of exchanging goods or services on credit.
    """


class NonCurrentAccountsReceivableBalanceSheet(MultiPeriodField):
    """
    Accounts receivable represents sums owed to the business that the business records as revenue. Gross accounts receivable is
    accounts receivable before the business deducts uncollectable accounts to calculate the true value of accounts receivable.
    """


class AccruedInterestReceivableBalanceSheet(MultiPeriodField):
    """
    This account shows the amount of unpaid interest accrued to the date of purchase and included in the purchase price of securities
    purchased between interest dates.
    """


class AdvanceFromFederalHomeLoanBanksBalanceSheet(MultiPeriodField):
    """
    This item is typically available for bank industry. It's the amount of borrowings as of the balance sheet date from the Federal Home
    Loan Bank, which are primarily used to cover shortages in the required reserve balance and liquidity shortages.
    """


class AllowanceForDoubtfulAccountsReceivableBalanceSheet(MultiPeriodField):
    """
    An Allowance for Doubtful Accounts measures receivables recorded but not expected to be collected.
    """


class AllowanceForNotesReceivableBalanceSheet(MultiPeriodField):
    """
    This item is typically available for bank industry. It represents a provision relating to a written agreement to receive money  with the
    terms of the note (at a specified future date(s) within one year from the reporting date (or the normal operating cycle, whichever is
    longer), consisting of principal as well as any accrued interest) for the portion that is expected to be uncollectible.
    """


class AssetsHeldForSaleBalanceSheet(MultiPeriodField):
    """
    This item is typically available for bank industry. It's a part of long-lived assets, which has been decided for sale in the future.
    """


class AssetsOfDiscontinuedOperationsBalanceSheet(MultiPeriodField):
    """
    A portion of a company's business that has been disposed of or sold.
    """


class BankIndebtednessBalanceSheet(MultiPeriodField):
    """
    All indebtedness for borrowed money or the deferred purchase price of property or services, including without limitation
    reimbursement and other obligations with respect to surety bonds and letters of credit, all obligations evidenced by notes, bonds
    debentures or similar instruments, all capital lease obligations and all contingent obligations.
    """


class BankOwnedLifeInsuranceBalanceSheet(MultiPeriodField):
    """
    The carrying amount of a life insurance policy on an officer, executive or employee for which the reporting entity (a bank) is entitled
    to proceeds from the policy upon death of the insured or surrender of the insurance policy.
    """


class SecurityBorrowedBalanceSheet(MultiPeriodField):
    """
    The securities borrowed or on loan, which is the temporary loan of securities by a lender to a borrower in exchange for cash.  This
    item is usually only available for bank industry.
    """


class BuildingsAndImprovementsBalanceSheet(MultiPeriodField):
    """
    Fixed assets that specifically deal with the facilities a company owns. Include the improvements associated with buildings.
    """


class CommercialLoanBalanceSheet(MultiPeriodField):
    """
    Short-term loan, typically 90 days, used by a company to finance seasonal working capital needs.
    """


class CommercialPaperBalanceSheet(MultiPeriodField):
    """
    Commercial paper is a money-market security issued by large banks and corporations. It represents the current obligation for the
    company. There are four basic kinds of commercial paper: promissory notes, drafts, checks, and certificates of deposit. The
    maturities of these money market securities generally do not exceed 270 days.
    """


class CommonStockEquityBalanceSheet(MultiPeriodField):
    """
    The portion of the Stockholders' Equity that reflects the amount of common stock, which are units of ownership.
    """


class ConstructionInProgressBalanceSheet(MultiPeriodField):
    """
    It represents carrying amount of long-lived asset under construction that includes construction costs to date on capital projects.
    Assets constructed, but not completed.
    """


class ConsumerLoanBalanceSheet(MultiPeriodField):
    """
    A loan that establishes consumer credit that is granted for personal use; usually unsecured and based on the borrower's integrity
    and ability to pay.
    """


class MinimumPensionLiabilitiesBalanceSheet(MultiPeriodField):
    """
    The company's minimum pension obligations to its former employees, paid into a defined pension plan to satisfy all pension
    entitlements that have been earned by employees to date.
    """


class CustomerAcceptancesBalanceSheet(MultiPeriodField):
    """
    Amounts receivable from customers on short-term negotiable time drafts drawn on and accepted by the institution (also known as
    banker's acceptance transactions) that are outstanding on the reporting date.
    """


class DefinedPensionBenefitBalanceSheet(MultiPeriodField):
    """
    The recognition of an asset where pension fund assets exceed promised benefits.
    """


class DerivativeProductLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Fair values of all liabilities resulting from contracts that meet the criteria of being accounted for as derivative instruments; and
    which are expected to be extinguished or otherwise disposed of after one year or beyond the normal operating cycle.
    """


class DerivativeAssetsBalanceSheet(MultiPeriodField):
    """
    Fair values of assets resulting from contracts that meet the criteria of being accounted for as derivative instruments, net of the
    effects of master netting arrangements.
    """


class DividendsPayableBalanceSheet(MultiPeriodField):
    """
    Sum of the carrying values of dividends declared but unpaid on equity securities issued and outstanding (also includes dividends
    collected on behalf of another owner of securities that are being held by entity) by the entity.
    """


class EmployeeBenefitsBalanceSheet(MultiPeriodField):
    """
    Carrying amount as of the balance sheet date of the portion of the obligations recognized for the various benefits provided to former
    or inactive employees, their beneficiaries, and covered dependents after employment but before retirement.
    """


class FederalFundsPurchasedBalanceSheet(MultiPeriodField):
    """
    The amount borrowed by a bank, at the federal funds rate, from another bank to meet its reserve requirements.  This item is
    typically available for the bank industry.
    """


class FederalFundsSoldBalanceSheet(MultiPeriodField):
    """
    Federal funds transactions involve lending (federal funds sold) or borrowing (federal funds purchased) of immediately available
    reserve balances.  This item is typically available for the bank industry.
    """


class FederalHomeLoanBankStockBalanceSheet(MultiPeriodField):
    """
    Federal Home Loan Bank stock represents an equity interest in a FHLB. It does not have a readily determinable fair value because
    its ownership is restricted and it lacks a market (liquidity).  This item is typically available for the bank industry.
    """


class FinancialAssetsBalanceSheet(MultiPeriodField):
    """
    Fair values as of the balance sheet date of all assets resulting from contracts that meet the criteria of being accounted for as
    derivative instruments, net of the effects of master netting arrangements.
    """


class FinancialInstrumentsSoldUnderAgreementsToRepurchaseBalanceSheet(MultiPeriodField):
    """
    The carrying value as of the balance sheet date of securities that an institution sells and agrees to repurchase (the identical or
    substantially the same securities) as a seller-borrower at a specified date for a specified price, also known as a repurchase
    agreement.  This item is typically available for bank industry.
    """


class FinishedGoodsBalanceSheet(MultiPeriodField):
    """
    The carrying amount as of the balance sheet date of merchandise or goods held by the company that are readily available for sale.
    This item is typically available for mining and manufacturing industries.
    """


class FlightFleetVehicleAndRelatedEquipmentsBalanceSheet(MultiPeriodField):
    """
    It is one of the important fixed assets for transportation industry, which includes bicycles, cars, motorcycles, trains, ships, boats,
    and aircraft.  This item is typically available for transportation industry.
    """


class ForeclosedAssetsBalanceSheet(MultiPeriodField):
    """
    The carrying amount as of the balance sheet date of all assets obtained in full or partial satisfaction of a debt arrangement through
    foreclosure proceedings or defeasance; includes real and personal property; equity interests in corporations, partnerships, and joint
    ventures; and beneficial interest in trusts.  This item is typically typically available for bank industry.
    """


class ForeignCurrencyTranslationAdjustmentsBalanceSheet(MultiPeriodField):
    """
    Changes to accumulated comprehensive income that results from the process of translating subsidiary financial statements and
    foreign equity investments into functional currency of the reporting company.
    """


class InventoriesAdjustmentsAllowancesBalanceSheet(MultiPeriodField):
    """
    This item represents certain charges made in the current period in inventory resulting from such factors as breakage, spoilage,
    employee theft and shoplifting. This item is typically available for manufacturing, mining and utility industries.
    """


class InvestmentsInOtherVenturesUnderEquityMethodBalanceSheet(MultiPeriodField):
    """
    This item represents the carrying amount on the company's balance sheet of its investments in common stock of an equity method.
    This item is typically available for the insurance industry.
    """


class LandAndImprovementsBalanceSheet(MultiPeriodField):
    """
    Fixed Assets that specifically deal with land a company owns. Includes the improvements associated with land. This excludes land
    held for sale.
    """


class LeasesBalanceSheet(MultiPeriodField):
    """
    Carrying amount at the balance sheet date of a long-lived, depreciable asset that is an addition or improvement to assets held
    under lease arrangement. This item is usually not available for the insurance industry.
    """


class LiabilitiesOfDiscontinuedOperationsBalanceSheet(MultiPeriodField):
    """
    The obligations arising from the sale, disposal, or planned sale in the near future (generally within one year) of a disposal group,
    including a component of the entity (discontinued operation). This item is typically available for bank industry.
    """


class LineOfCreditBalanceSheet(MultiPeriodField):
    """
    The carrying value as of the balance sheet date of obligations drawn from a line of credit, which is a bank's commitment to make
    loans up to a specific amount.
    """


class LoansHeldForSaleBalanceSheet(MultiPeriodField):
    """
    It means the aggregate amount of loans receivable that will be sold to other entities.  This item is typically available for bank
    industry.
    """


class LoansReceivableBalanceSheet(MultiPeriodField):
    """
    Reflects the carrying amount of unpaid loans issued to other institutions for cash needs or an asset purchase.
    """


class MachineryFurnitureEquipmentBalanceSheet(MultiPeriodField):
    """
    Fixed assets specifically dealing with tools, equipment and office furniture. This item is usually not available for the insurance and
    utility industries.
    """


class MaterialsAndSuppliesBalanceSheet(MultiPeriodField):
    """
    Aggregated amount of unprocessed materials to be used in manufacturing or production process and supplies that will be
    consumed. This item is typically available for the utility industry.
    """


class MineralPropertiesBalanceSheet(MultiPeriodField):
    """
    A fixed asset that represents strictly mineral type properties.  This item is typically available for mining industry.
    """


class MortgageLoanBalanceSheet(MultiPeriodField):
    """
    This is a lien on real estate to protect a lender.  This item is typically available for bank industry.
    """


class MortgageAndConsumerloansBalanceSheet(MultiPeriodField):
    """
    It means the aggregate amount of mortgage and consumer loans.  This item is typically available for the insurance industry.
    """


class GrossNotesReceivableBalanceSheet(MultiPeriodField):
    """
    An amount representing an agreement for an unconditional promise by the maker to pay the entity (holder) a definite sum of money
    at a future date(s) within one year of the balance sheet date or the normal operating cycle. Such amount may include accrued
    interest receivable in accordance with the terms of the note. The note also may contain provisions including a discount or premium,
    payable on demand, secured, or unsecured, interest bearing or non-interest bearing, among myriad other features and
    characteristics. This item is typically available for bank industry.
    """


class OtherAssetsBalanceSheet(MultiPeriodField):
    """
    Other non-current assets that are not otherwise classified.
    """


class OtherCapitalStockBalanceSheet(MultiPeriodField):
    """
    Other Capital Stock that is not otherwise classified.
    """


class OtherCurrentAssetsBalanceSheet(MultiPeriodField):
    """
    Other current assets that are not otherwise classified.
    """


class OtherCurrentBorrowingsBalanceSheet(MultiPeriodField):
    """
    Short Term Borrowings that are not otherwise classified.
    """


class OtherEquityAdjustmentsBalanceSheet(MultiPeriodField):
    """
    Other adjustments to stockholders' equity that is not otherwise classified, including other reserves.
    """


class OtherInventoriesBalanceSheet(MultiPeriodField):
    """
    Other non-current inventories not otherwise classified.
    """


class OtherInvestedAssetsBalanceSheet(MultiPeriodField):
    """
    An item represents all the other investments or/and securities that cannot be defined into any category above. This item is typically
    available for the insurance industry.
    """


class OtherNonCurrentAssetsBalanceSheet(MultiPeriodField):
    """
    Other non-current assets that are not otherwise classified.
    """


class OtherPropertiesBalanceSheet(MultiPeriodField):
    """
    Other fixed assets not otherwise classified.
    """


class OtherRealEstateOwnedBalanceSheet(MultiPeriodField):
    """
    The Carrying amount as of the balance sheet date of other real estate, which may include real estate investments, real estate loans
    that qualify as investments in real estate, and premises that are no longer used in operations may also be included in real estate
    owned. This does not include real estate assets taken in settlement of troubled loans through surrender or foreclosure.  This item is
    typically available for bank industry.
    """


class OtherReceivablesBalanceSheet(MultiPeriodField):
    """
    Other non-current receivables not otherwise classified.
    """


class NonCurrentPensionAndOtherPostretirementBenefitPlansBalanceSheet(MultiPeriodField):
    """
    A loan issued by an insurance company that uses the cash value of a person's life insurance policy as collateral.  This item is usually
    only available in the insurance industry.
    """


class PolicyLoansBalanceSheet(MultiPeriodField):
    """
    A loan issued by an insurance company that uses the cash value of a person's life insurance policy as collateral. This item is usually
    only available for insurance industry.
    """


class PreferredStockEquityBalanceSheet(MultiPeriodField):
    """
    A class of ownership in a company that has a higher claim on the assets and earnings than common stock. Preferred stock
    generally has a dividend that must be paid out before dividends to common stockholders and the shares usually do not have voting
    rights.
    """


class PropertiesBalanceSheet(MultiPeriodField):
    """
    Tangible assets that are held by an entity for use in the production or supply of goods and services, for rental to others, or for
    administrative purposes and that are expected to provide economic benefit for more than one year. This item is available for
    manufacturing, bank and transportation industries.
    """


class CurrentProvisionsBalanceSheet(MultiPeriodField):
    """
    Provisions are created to protect the interests of one or both parties named in a contract or legal document which is a preparatory
    action or measure. Current provision is expired within one accounting PeriodAsByte.
    """


class LongTermProvisionsBalanceSheet(MultiPeriodField):
    """
    Provisions are created to protect the interests of one or both parties named in a contract or legal document which is a preparatory
    action or measure. Long-term provision is expired beyond one accounting PeriodAsByte.
    """


class RawMaterialsBalanceSheet(MultiPeriodField):
    """
    Carrying amount as of the balance sheet data of unprocessed items to be consumed in the manufacturing or production process.
    This item is available for manufacturing and mining industries.
    """


class ReceivablesAdjustmentsAllowancesBalanceSheet(MultiPeriodField):
    """
    A provision relating to a written agreement to receive money at a specified future date(s) (within one year from the reporting date
    or the normal operating cycle, whichever is longer), consisting of principal as well as any accrued interest).
    """


class RegulatoryAssetsBalanceSheet(MultiPeriodField):
    """
    Carrying amount as of the balance sheet date of capitalized costs of regulated entities that are expected to be recovered through
    revenue sources over one year or beyond the normal operating cycle.
    """


class RegulatoryLiabilitiesBalanceSheet(MultiPeriodField):
    """
    The amount for the individual regulatory noncurrent liability as itemized in a table of regulatory noncurrent liabilities as of the end of
    the PeriodAsByte. Such things as the costs of energy efficiency programs and low-income energy assistances programs and deferred fuel.
    This item is usually only available for utility industry.
    """


class ReinsuranceBalancesPayableBalanceSheet(MultiPeriodField):
    """
    The carrying amount as of the balance sheet date of the known and estimated amounts owed to insurers under reinsurance
    treaties or other arrangements. This item is usually only available for insurance industry.
    """


class RestrictedCashBalanceSheet(MultiPeriodField):
    """
    The carrying amounts of cash and cash equivalent items, which are restricted as to withdrawal or usage. Restrictions may include
    legally restricted deposits held as compensating balances against short-term borrowing arrangements, contracts entered into with
    others, or entity statements of intention with regard to particular deposits; however, time deposits and short-term certificates of
    deposit are not generally included in legally restricted deposits. Excludes compensating balance arrangements that are not
    agreements, which legally restrict the use of cash amounts shown on the balance sheet. For a classified balance sheet, represents
    the current portion only (the non-current portion has a separate concept); for an unclassified balance sheet represents the entire
    amount. This item is usually not available for bank and insurance industries.
    """


class RestrictedCashAndCashEquivalentsBalanceSheet(MultiPeriodField):
    """
    The carrying amounts of cash and cash equivalent items which are restricted as to withdrawal or usage. This item is available for
    bank and insurance industries.
    """


class RestrictedCashAndInvestmentsBalanceSheet(MultiPeriodField):
    """
    The cash and investments whose use in whole or in part is restricted for the long-term, generally by contractual agreements or
    regulatory requirements. This item is usually only available for bank industry.
    """


class RestrictedCommonStockBalanceSheet(MultiPeriodField):
    """
    Shares of stock for which sale is contractually or governmentally restricted for a given period of time. Stock that is acquired through
    an employee stock option plan or other private means may not be transferred. Restricted stock must be traded in compliance with
    special SEC regulations.
    """


class RestrictedInvestmentsBalanceSheet(MultiPeriodField):
    """
    Investments whose use is restricted in whole or in part, generally by contractual agreements or regulatory requirements. This item
    is usually only available for bank industry.
    """


class TaxesReceivableBalanceSheet(MultiPeriodField):
    """
    Carrying amount due within one year of the balance sheet date (or one operating cycle, if longer) from tax authorities as of the
    balance sheet date representing refunds of overpayments or recoveries based on agreed-upon resolutions of disputes. This item is
    usually not available for bank industry.
    """


class TotalCapitalizationBalanceSheet(MultiPeriodField):
    """
    Stockholder's Equity plus Long Term Debt.
    """


class TotalDeferredCreditsAndOtherNonCurrentLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Revenue received by a firm but not yet reported as income.  This item is usually only available for utility industry.
    """


class UnbilledReceivablesBalanceSheet(MultiPeriodField):
    """
    Revenues that are not currently billed from the customer under the terms of the contract.  This item is usually only available for
    utility industry.
    """


class UnrealizedGainLossBalanceSheet(MultiPeriodField):
    """
    A profit or loss that results from holding onto an asset rather than cashing it in and officially taking the profit or loss.
    """


class WorkInProcessBalanceSheet(MultiPeriodField):
    """
    Work, or goods, in the process of being fabricated or manufactured but not yet completed as finished goods. This item is usually
    available for manufacturing and mining industries.
    """


class OtherNonCurrentLiabilitiesBalanceSheet(MultiPeriodField):
    """
    This item is usually not available for bank and insurance industries.
    """


class CapitalLeaseObligationsBalanceSheet(MultiPeriodField):
    """
    Current Portion of Capital Lease Obligation plus Long Term Portion of Capital Lease Obligation.
    """


class OtherLiabilitiesBalanceSheet(MultiPeriodField):
    """
    This item is available for bank and insurance industries.
    """


class OtherPayableBalanceSheet(MultiPeriodField):
    """
    Payables and Accrued Expenses that are not defined as Trade, Tax or Dividends related.
    """


class TangibleBookValueBalanceSheet(MultiPeriodField):
    """
    The company's total book value less the value of any intangible assets.
    Methodology: Common Stock Equity minus Goodwill and Other Intangible Assets
    """


class TotalEquityBalanceSheet(MultiPeriodField):
    """
    Total Equity equals Preferred Stock Equity + Common Stock Equity.
    """


class WorkingCapitalBalanceSheet(MultiPeriodField):
    """
    Current Assets minus Current Liabilities.  This item is usually not available for bank and insurance industries.
    """


class TotalDebtBalanceSheet(MultiPeriodField):
    """
    All borrowings incurred by the company including debt and capital lease obligations.
    """


class CommonUtilityPlantBalanceSheet(MultiPeriodField):
    """
    The amount for the other plant related to the utility industry fix assets.
    """


class ElectricUtilityPlantBalanceSheet(MultiPeriodField):
    """
    The amount for the electric plant related to the utility industry.
    """


class NaturalGasFuelAndOtherBalanceSheet(MultiPeriodField):
    """
    The amount for the natural gas, fuel and other items related to the utility industry, which might include oil and gas wells, the
    properties to exploit oil and gas or liquefied natural gas sites.
    """


class NetUtilityPlantBalanceSheet(MultiPeriodField):
    """
    Net utility plant might include water production, electric utility plan, natural gas, fuel and other, common utility plant and
    accumulated depreciation. This item is usually only available for utility industry.
    """


class WaterProductionBalanceSheet(MultiPeriodField):
    """
    The amount for a facility and plant that provides water which might include wells, reservoirs, pumping stations, and control
    facilities; and waste water systems which includes the waste treatment and disposal facility and equipment. This item is usually
    only available for utility industry.
    """


class OrdinarySharesNumberBalanceSheet(MultiPeriodField):
    """
    Number of Common or Ordinary Shares.
    """


class PreferredSharesNumberBalanceSheet(MultiPeriodField):
    """
    Number of Preferred Shares.
    """


class TreasurySharesNumberBalanceSheet(MultiPeriodField):
    """
    Number of Treasury Shares.
    """


class TradingAndOtherReceivableBalanceSheet(MultiPeriodField):
    """
    This will serve as the "parent" value to AccountsReceivable (DataId 23001) and OtherReceivables (DataId 23342) for all company
    financials reported in the IFRS GAAP.
    """


class EquityAttributableToOwnersOfParentBalanceSheet(MultiPeriodField):
    """
    
    """


class SecuritiesLoanedBalanceSheet(MultiPeriodField):
    """
    The carrying value as of the balance sheet date of securities loaned to other broker dealers, typically used by such parties to cover
    short sales, secured by cash or other securities furnished by such parties until the borrowing is closed.
    """


class NetTangibleAssetsBalanceSheet(MultiPeriodField):
    """
    Net assets in physical form. This is calculated using Stockholders' Equity less Intangible Assets (including Goodwill).
    """


class DuefromRelatedPartiesCurrentBalanceSheet(MultiPeriodField):
    """
    Amounts owed to the company from a non-arm's length entity, due within the company's current operating cycle.
    """


class DuefromRelatedPartiesNonCurrentBalanceSheet(MultiPeriodField):
    """
    Amounts owed to the company from a non-arm's length entity, due after the company's current operating cycle.
    """


class DuetoRelatedPartiesBalanceSheet(MultiPeriodField):
    """
    Amounts owed by the company to a non-arm's length entity.
    """


class DuetoRelatedPartiesCurrentBalanceSheet(MultiPeriodField):
    """
    Amounts owed by the company to a non-arm's length entity that has to be repaid within the company's current operating cycle.
    """


class DuetoRelatedPartiesNonCurrentBalanceSheet(MultiPeriodField):
    """
    Amounts owed by the company to a non-arm's length entity that has to be repaid after the company's current operating cycle.
    """


class InvestmentPropertiesBalanceSheet(MultiPeriodField):
    """
    Company's investments in properties net of accumulated depreciation, which generate a return.
    """


class InvestmentsinSubsidiariesatCostBalanceSheet(MultiPeriodField):
    """
    A stake in any company which is more than 51%.
    """


class InvestmentsinAssociatesatCostBalanceSheet(MultiPeriodField):
    """
    A stake in any company which is more than 20% but less than 50%.
    """


class InvestmentsinJointVenturesatCostBalanceSheet(MultiPeriodField):
    """
    A 50% stake in any company in which remaining 50% belongs to other company.
    """


class InvestmentinFinancialAssetsBalanceSheet(MultiPeriodField):
    """
    Represents the sum of all financial investments (trading securities, available-for-sale securities, held-to-maturity securities, etc.)
    """


class FinanceLeaseReceivablesBalanceSheet(MultiPeriodField):
    """
    Accounts owed to the bank in relation to capital leases. Capital/ finance lease obligation are contractual obligations that arise from
    obtaining the use of property or equipment via a capital lease contract.
    """


class ConvertibleLoansCurrentBalanceSheet(MultiPeriodField):
    """
    This represents loans that entitle the lender (or the holder of loan debenture) to convert the loan to common or preferred stock
    (ordinary or preference shares) within the next 12 months or operating cycle.
    """


class BankLoansCurrentBalanceSheet(MultiPeriodField):
    """
    A debt financing obligation issued by a bank or similar financial institution to a company, that entitles the lender or holder of the
    instrument to interest payments and the repayment of principal at a specified time within the next 12 months or operating cycle.
    """


class OtherLoansCurrentBalanceSheet(MultiPeriodField):
    """
    Other loans between the customer and bank which cannot be identified by other specific items in the Debt section, due within the
    next 12 months or operating cycle.
    """


class AccruedandDeferredIncomeBalanceSheet(MultiPeriodField):
    """
    Sum of accrued liabilities and deferred income (amount received in advance but the services are not provided in respect of
    amount).
    """


class BankLoansNonCurrentBalanceSheet(MultiPeriodField):
    """
    A debt financing obligation issued by a bank or similar financial institution to a company, that entitles the lender or holder of the
    instrument to interest payments and the repayment of principal at a specified time beyond the current accounting PeriodAsByte.
    """


class OtherLoansNonCurrentBalanceSheet(MultiPeriodField):
    """
    Other loans between the customer and bank which cannot be identified by other specific items in the Debt section, due beyond the
    current operating cycle.
    """


class OtherReservesBalanceSheet(MultiPeriodField):
    """
    Other reserves owned by the company that cannot be identified by other specific items in the Reserves section.
    """


class LoansandAdvancestoBankBalanceSheet(MultiPeriodField):
    """
    The aggregate amount of loans and advances made to a bank or financial institution.
    """


class LoansandAdvancestoCustomerBalanceSheet(MultiPeriodField):
    """
    The aggregate amount of loans and advances made to customers.
    """


class TreasuryBillsandOtherEligibleBillsBalanceSheet(MultiPeriodField):
    """
    Investments backed by the central government, it usually carries less risk than other investments.
    """


class EquitySharesInvestmentsBalanceSheet(MultiPeriodField):
    """
    Investments in shares of a company representing ownership in that company.
    """


class DepositsbyBankBalanceSheet(MultiPeriodField):
    """
    Banks investment in the ongoing entity.
    """


class CustomerAccountsBalanceSheet(MultiPeriodField):
    """
    Carrying value of amounts transferred by customers to third parties for security purposes that are expected to be returned or
    applied towards payment after one year or beyond the operating cycle, if longer.
    """


class ItemsinTheCourseofTransmissiontoOtherBanksBalanceSheet(MultiPeriodField):
    """
    Carrying amount as of the balance sheet date of drafts and bills of exchange that have been accepted by the reporting bank or by
    others for its own account, as its liability to holders of the drafts.
    """


class TradingandFinancialLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Total carrying amount of total trading, financial liabilities and debt in a non-differentiated balance sheet.
    """


class DebtSecuritiesinIssueBalanceSheet(MultiPeriodField):
    """
    Any debt financial instrument issued instead of cash loan.
    """


class SubordinatedLiabilitiesBalanceSheet(MultiPeriodField):
    """
    The total carrying value of securities loaned to other broker dealers, typically used by such parties to cover short sales, secured by
    cash or other securities furnished by such parties until the borrowing is closed; in a Non-Differentiated Balance Sheet.
    """


class ProvisionsTotalBalanceSheet(MultiPeriodField):
    """
    Provisions are created to protect the interests of one or both parties named in a contract or legal document, which is a preparatory
    action or measure. Current provision is expired within one accounting PeriodAsByte.
    """


class OperatingLeaseAssetsBalanceSheet(MultiPeriodField):
    """
    A contract that allows for the use of an asset, but does not convey rights of ownership of the asset. An operating lease is not
    capitalized; it is accounted for as a rental expense in what is known as "off balance sheet financing." For the lessor, the asset being
    leased is accounted for as an asset and is depreciated as such.
    """


class ClaimsOutstandingBalanceSheet(MultiPeriodField):
    """
    Amounts owing to policy holders who have filed claims but have not yet been settled or paid.
    """


class LiabilitiesHeldforSaleCurrentBalanceSheet(MultiPeriodField):
    """
    Liabilities due within the next 12 months related from an asset classified as Held for Sale.
    """


class LiabilitiesHeldforSaleNonCurrentBalanceSheet(MultiPeriodField):
    """
    Liabilities related to an asset classified as held for sale excluding the portion due the next 12 months or operating cycle.
    """


class DebtSecuritiesBalanceSheet(MultiPeriodField):
    """
    Debt securities held as investments.
    """


class TotalFinancialLeaseObligationsBalanceSheet(MultiPeriodField):
    """
    Represents the total amount of long-term capital leases that must be paid within the next accounting period for a Non-
    Differentiated Balance Sheet. Capital lease obligations are contractual obligations that arise from obtaining the use of property or
    equipment via a capital lease contract.
    """


class AccruedandDeferredIncomeCurrentBalanceSheet(MultiPeriodField):
    """
    Sum of Accrued Liabilities and Deferred Income (amount received in advance but the services are not provided in respect of
    amount) due within 1 year.
    """


class AccruedandDeferredIncomeNonCurrentBalanceSheet(MultiPeriodField):
    """
    Sum of Accrued Liabilities and Deferred Income (amount received in advance but the services are not provided in respect of
    amount) due after 1 year.
    """


class FinanceLeaseReceivablesCurrentBalanceSheet(MultiPeriodField):
    """
    Accounts owed to the bank in relation to capital leases to be received within the next accounting PeriodAsByte. Capital/ finance lease
    obligations are contractual obligations that arise from obtaining the use of property or equipment via a capital lease contract.
    """


class FinanceLeaseReceivablesNonCurrentBalanceSheet(MultiPeriodField):
    """
    Accounts owed to the bank in relation to capital leases to be received beyond the next accounting PeriodAsByte. Capital/ finance lease
    obligations are contractual obligations that arise from obtaining the use of property or equipment via a capital lease contract.
    """


class FinancialLiabilitiesCurrentBalanceSheet(MultiPeriodField):
    """
    Financial related liabilities due within one year, including short term and current portions of long-term debt, capital leases and
    derivative liabilities.
    """


class FinancialLiabilitiesNonCurrentBalanceSheet(MultiPeriodField):
    """
    Financial related liabilities due beyond one year, including long term debt, capital leases and derivative liabilities.
    """


class FinancialAssetsDesignatedasFairValueThroughProfitorLossTotalBalanceSheet(MultiPeriodField):
    """
    Financial assets that are held at fair value through profit or loss comprise assets held for trading and those financial assets
    designated as being held at fair value through profit or loss.
    """


class TaxesAssetsCurrentBalanceSheet(MultiPeriodField):
    """
    Carrying amount due within one year of the balance sheet date (or one operating cycle, if longer) from tax authorities as of the
    balance sheet date representing refunds of overpayments or recoveries based on agreed-upon resolutions of disputes, and current
    deferred tax assets.
    """


class OtherEquityInterestBalanceSheet(MultiPeriodField):
    """
    Other equity instruments issued by the company that cannot be identified by other specific items in the Equity section.
    """


class InterestBearingBorrowingsNonCurrentBalanceSheet(MultiPeriodField):
    """
    Carrying amount of any interest-bearing loan which is due after one year.
    """


class NonInterestBearingBorrowingsNonCurrentBalanceSheet(MultiPeriodField):
    """
    Non-interest bearing borrowings due after a year.
    """


class TradeandOtherPayablesNonCurrentBalanceSheet(MultiPeriodField):
    """
    Sum of all non-current payables and accrued expenses.
    """


class NonInterestBearingBorrowingsCurrentBalanceSheet(MultiPeriodField):
    """
    Non-interest bearing deposits in other financial institutions for short periods of time, usually less than 12 months.
    """


class PensionandOtherPostRetirementBenefitPlansCurrentBalanceSheet(MultiPeriodField):
    """
    Total of the carrying values as of the balance sheet date of obligations incurred through that date and payable for obligations related
    to services received from employees, such as accrued salaries and bonuses, payroll taxes and fringe benefits.
    """


class OtherLoanAssetsBalanceSheet(MultiPeriodField):
    """
    Reflects the carrying amount of any other unpaid loans, an asset of the bank.
    """


class AssetsPledgedasCollateralSubjecttoSaleorRepledgingTotalBalanceSheet(MultiPeriodField):
    """
    Total value collateral assets pledged to the bank that can be sold or used as collateral for other loans.
    """


class TaxAssetsTotalBalanceSheet(MultiPeriodField):
    """
    Sum of total tax assets in a Non-Differentiated Balance Sheet, includes Tax Receivables and Deferred Tax Assets.
    """


class AdvancesfromCentralBanksBalanceSheet(MultiPeriodField):
    """
    Borrowings from the central bank, which are primarily used to cover shortages in the required reserve balance and liquidity
    shortages.
    """


class DepositCertificatesBalanceSheet(MultiPeriodField):
    """
    A savings certificate entitling the bearer to receive interest. A CD bears a maturity date, a specified fixed interest rate and can be
    issued in any denomination.
    """


class NonInterestBearingBorrowingsTotalBalanceSheet(MultiPeriodField):
    """
    Non-interest bearing deposits in other financial institutions for relatively short periods of time; on a Non-Differentiated Balance
    Sheet.
    """


class OtherBorrowedFundsBalanceSheet(MultiPeriodField):
    """
    Other borrowings by the bank to fund its activities that cannot be identified by other specific items in the Liabilities section.
    """


class FinancialLiabilitiesDesignatedasFairValueThroughProfitorLossTotalBalanceSheet(MultiPeriodField):
    """
    Financial liabilities that are held at fair value through profit or loss.
    """


class FinancialLiabilitiesMeasuredatAmortizedCostTotalBalanceSheet(MultiPeriodField):
    """
    Financial liabilities carried at amortized cost.
    """


class AccruedLiabilitiesTotalBalanceSheet(MultiPeriodField):
    """
    Liabilities which have occurred, but have not been paid or logged under accounts payable during an accounting PeriodAsByte. In other
    words, obligations for goods and services provided to a company for which invoices have not yet been received; on a Non-
    Differentiated Balance Sheet.
    """


class DeferredIncomeTotalBalanceSheet(MultiPeriodField):
    """
    Collections of cash or other assets related to revenue producing activity for which revenue has not yet been recognized on a Non-
    Differentiated Balance Sheet.
    """


class DeferredTaxLiabilitiesTotalBalanceSheet(MultiPeriodField):
    """
    A future tax liability, resulting from temporary differences between book (accounting) value of assets and liabilities and their tax
    value or timing differences between the recognition of gains and losses in financial statements, on a Non-Differentiated Balance
    Sheet.
    """


class ReinsuranceAssetsBalanceSheet(MultiPeriodField):
    """
    Reinsurance asset is insurance that is purchased by an insurance company from another insurance company.
    """


class DepositsMadeunderAssumedReinsuranceContractBalanceSheet(MultiPeriodField):
    """
    Deposits made under reinsurance.
    """


class InsuranceContractAssetsBalanceSheet(MultiPeriodField):
    """
    A contract under which one party (the insurer) accepts significant insurance risk from another party (the policyholder) by agreeing
    to compensate the policyholder if a specified uncertain future event (the insured event) adversely affects the policyholder. This
    includes Insurance Receivables and Premiums Receivables.
    """


class InsuranceContractLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Any type of insurance policy that protects an individual or business from the risk that they may be sued and held legally liable for
    something such as malpractice, injury or negligence. Liability insurance policies cover both legal costs and any legal payouts for
    which the insured would be responsible if found legally liable. Intentional damage and contractual liabilities are typically not covered
    in these types of policies.
    """


class DepositsReceivedunderCededInsuranceContractBalanceSheet(MultiPeriodField):
    """
    Deposit received through ceded insurance contract.
    """


class InvestmentContractLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Liabilities due on the insurance investment contract.
    """


class PensionAndOtherPostretirementBenefitPlansTotalBalanceSheet(MultiPeriodField):
    """
    Total of the carrying values as of the balance sheet date of obligations incurred through that date and payable for obligations related
    to services received from employees, such as accrued salaries and bonuses, payroll taxes and fringe benefits. Used to reflect the
    current portion of the liabilities (due within one year or within the normal operating cycle if longer).
    """


class LiabilitiesHeldforSaleTotalBalanceSheet(MultiPeriodField):
    """
    Liabilities related to an asset classified as held for sale.
    """


class HedgingAssetsCurrentBalanceSheet(MultiPeriodField):
    """
    A security transaction which expires within a 12 month period that reduces the risk on an existing investment position.
    """


class ConvertibleLoansTotalBalanceSheet(MultiPeriodField):
    """
    Loans that entitles the lender (or the holder of loan debenture) to convert the loan to common or preferred stock (ordinary or
    preference shares) at a specified rate conversion rate and a specified time frame; in a Non-Differentiated Balance Sheet.
    """


class BankLoansTotalBalanceSheet(MultiPeriodField):
    """
    Total debt financing obligation issued by a bank or similar financial institution to a company that entitles the lender or holder of the
    instrument to interest payments and the repayment of principal at a specified time; in a Non-Differentiated Balance Sheet.
    """


class OtherLoansTotalBalanceSheet(MultiPeriodField):
    """
    Total other loans between the customer and bank which cannot be identified by other specific items in the Debt section; in a Non-
    Differentiated Balance Sheet.
    """


class InsuranceFundsNonCurrentBalanceSheet(MultiPeriodField):
    """
    Liabilities related to insurance funds that are dissolved after one year.
    """


class DebtTotalBalanceSheet(MultiPeriodField):
    """
    The total aggregate of all written promises and/or agreements to repay a stated amount of borrowed funds at a specified date in
    the future; in a Non-Differentiated Balance Sheet.
    """


class ComTreShaNumBalanceSheet(MultiPeriodField):
    """
    The treasury stock number of common shares. This represents the number of common shares owned by the company as a result of
    share repurchase programs or donations.
    """


class PreTreShaNumBalanceSheet(MultiPeriodField):
    """
    The treasury stock number of preferred shares. This represents the number of preferred shares owned by the company as a result
    of share repurchase programs or donations.
    """


class NetDebtBalanceSheet(MultiPeriodField):
    """
    This is a metric that shows a company's overall debt situation by netting the value of a company's liabilities and
    debts with its cash and other similar liquid assets. It is calculated using [Current Debt] + [Long Term Debt] - [Cash and Cash
    Equivalents].
    """


class ShareIssuedBalanceSheet(MultiPeriodField):
    """
    The number of authorized shares that is sold to and held by the shareholders of a company, regardless of whether they are insiders,
    institutional investors or the general public. Unlike shares that are held as treasury stock, shares that have been retired are not
    included in this figure. The amount of issued shares can be all or part of the total amount of authorized shares of a corporation.
    """


class AssetsHeldForSaleCurrentBalanceSheet(MultiPeriodField):
    """
    Short term assets set apart for sale to liquidate in the future and are measured at the lower of carrying amount and fair value less
    costs to sell.
    """


class AssetsHeldForSaleNonCurrentBalanceSheet(MultiPeriodField):
    """
    Long term assets set apart for sale to liquidate in the future and are measured at the lower of carrying amount and fair value less
    costs to sell.
    """


class BiologicalAssetsBalanceSheet(MultiPeriodField):
    """
    Biological assets include plants and animals.
    """


class CashRestrictedOrPledgedBalanceSheet(MultiPeriodField):
    """
    Cash that the company can use only for specific purposes or cash deposit or placing of owned property by a debtor (the pledger) to
    a creditor (the pledgee) as a security for a loan or obligation.
    """


class ConvertibleLoansNonCurrentBalanceSheet(MultiPeriodField):
    """
    A long term loan with a warrant attached that gives the debt holder the option to exchange all or a portion of the loan principal for
    an equity position in the company at a predetermined rate of conversion within a specified period of time.
    """


class FinancialOrDerivativeInvestmentCurrentLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Financial instruments that are linked to a specific financial instrument or indicator or commodity, and through which specific
    financial risks can be traded in financial markets in their own right, such as financial options, futures, forwards, etc.
    """


class OtherInvestmentsBalanceSheet(MultiPeriodField):
    """
    Investments that are neither Investment in Financial Assets nor Long term equity investment, not expected to be cashed within a
    year.
    """


class TradeAndOtherReceivablesNonCurrentBalanceSheet(MultiPeriodField):
    """
    Amounts due from customers or clients, more than one year from the balance sheet date, for goods or services that have been
    delivered or sold in the normal course of business, or other receivables.
    """


class DueFromRelatedPartiesBalanceSheet(MultiPeriodField):
    """
    For an unclassified balance sheet, carrying amount as of the balance sheet date of obligations due all related parties.
    """


class UnallocatedSurplusBalanceSheet(MultiPeriodField):
    """
    The amount of surplus from insurance contracts which has not been allocated at the balance sheet date. This is represented as a
    liability to policyholders, as it pertains to cumulative income arising from the with-profits business.
    """


class DebtDueInYear1BalanceSheet(MultiPeriodField):
    """
    Debt due under 1 year according to the debt maturity schedule reported by the company.
    """


class DebtDueInYear2BalanceSheet(MultiPeriodField):
    """
    Debt due under 2 years according to the debt maturity schedule reported by the company.
    """


class DebtDueInYear5BalanceSheet(MultiPeriodField):
    """
    Debt due within 5 year if the company provide maturity schedule in range e.g. 1-5 years, 2-5 years. Debt due under 5 years
    according to the debt maturity schedule reported by the company. If a range is reported by the company, the value will be collected
    under the maximum number of years (eg. 1-5 years, 3-5 years or 5 years will all be collected under this data point.)
    """


class DebtDueBeyondBalanceSheet(MultiPeriodField):
    """
    Debt maturing beyond 5 years (eg. 5-10 years) or with no specified maturity, according to the debt maturity schedule reported by
    the company.
    """


class TotalDebtInMaturityScheduleBalanceSheet(MultiPeriodField):
    """
    Total Debt in Maturity Schedule is the sum of Debt details above.
    """


class FixedAssetsRevaluationReserveBalanceSheet(MultiPeriodField):
    """
    Reserves created by revaluation of assets.
    """


class CurrentOtherFinancialLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Other short term financial liabilities not categorized and due within one year or a normal operating cycle (whichever is longer).
    """


class NonCurrentOtherFinancialLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Other long term financial liabilities not categorized and due over one year or a normal operating cycle (whichever is longer).
    """


class OtherFinancialLiabilitiesBalanceSheet(MultiPeriodField):
    """
    Other financial liabilities not categorized.
    """


class TotalLiabilitiesAsReportedBalanceSheet(MultiPeriodField):
    """
    Total liabilities as reported by the company, may be the same or not the same as Morningstar's standardized definition.
    """


class TotalEquityAsReportedBalanceSheet(MultiPeriodField):
    """
    Total Equity as reported by the company, may be the same or not the same as Morningstar's standardized definition.
    """


class AmortizationCashFlowStatement(MultiPeriodField):
    """
    The systematic and rational apportionment of the acquisition cost of intangible operational assets to future periods in which the benefits
    contribute to revenue. This field is to include Amortization and any variation where Amortization is the first account listed in the line item,
    excluding Amortization of Intangibles.
    """


class CapitalExpenditureCashFlowStatement(MultiPeriodField):
    """
    Funds used by a company to acquire or upgrade physical assets such as property, industrial buildings or equipment. This
    type of outlay is made by companies to maintain or increase the scope of their operations. Capital expenditures are generally
    depreciated or depleted over their useful life, as distinguished from repairs, which are subtracted from the income of the current
    year.
    """


class CashDividendsPaidCashFlowStatement(MultiPeriodField):
    """
    Payments for the cash dividends declared by an entity to shareholders during the PeriodAsByte. This element includes paid and unpaid
    dividends declared during the period for both common and preferred stock.
    """


class CashFlowFromContinuingFinancingActivitiesCashFlowStatement(MultiPeriodField):
    """
    Cash generated by or used in financing activities of continuing operations; excludes cash flows from discontinued operations.
    """


class CashFlowFromContinuingInvestingActivitiesCashFlowStatement(MultiPeriodField):
    """
    Cash generated by or used in investing activities of continuing operations; excludes cash flows from discontinued operations.
    """


class CashFlowFromContinuingOperatingActivitiesCashFlowStatement(MultiPeriodField):
    """
    Cash generated by or used in operating activities of continuing operations; excludes cash flows from discontinued operations.
    """


class CashFlowFromDiscontinuedOperationCashFlowStatement(MultiPeriodField):
    """
    The aggregate amount of cash flow from discontinued operation, including operating activities, investing activities, and financing
    activities.
    """


class FinancingCashFlowCashFlowStatement(MultiPeriodField):
    """
    The net cash inflow (outflow) from financing activity for the period, which involve changes to the long-term liabilities and
    stockholders' equity.
    """


class InvestingCashFlowCashFlowStatement(MultiPeriodField):
    """
    An item on the cash flow statement that reports the aggregate change in a company's cash position resulting from any gains (or
    losses) from investments in the financial markets and operating subsidiaries, and changes resulting from amounts spent on
    investments in capital assets such as plant and equipment.
    """


class OperatingCashFlowCashFlowStatement(MultiPeriodField):
    """
    The net cash from (used in) all of the entity's operating activities, including those of discontinued operations, of the reporting entity.
    Operating activities include all transactions and events that are not defined as investing or financing activities. Operating activities
    generally involve producing and delivering goods and providing services. Cash flows from operating activities are generally the cash
    effects of transactions and other events that enter into the determination of net income.
    """


class BeginningCashPositionCashFlowStatement(MultiPeriodField):
    """
    The cash and equivalents balance at the beginning of the accounting period, as indicated on the Cash Flow statement.
    """


class EndCashPositionCashFlowStatement(MultiPeriodField):
    """
    The cash and cash equivalents balance at the end of the accounting period, as indicated on the Cash Flow statement. It is equal to
    the Beginning Cash and Equivalents, plus the Net Change in Cash and Equivalents.
    """


class CashFromDiscontinuedFinancingCashFlowStatement(MultiPeriodField):
    """
    Cash generated by or used in financing activities of discontinued operations; excludes cash flows from continued operations.
    """


class CashFromDiscontinuedFinancingActivitiesCashFlowStatement(MultiPeriodField):
    """
    Cash generated by or used in financing activities of discontinued operations; excludes cash flows from continued operations.
    """


class CashFromDiscontinuedInvestingCashFlowStatement(MultiPeriodField):
    """
    The net cash inflow (outflow) from discontinued investing activities over the designated time PeriodAsByte.
    """


class CashFromDiscontinuedInvestingActivitiesCashFlowStatement(MultiPeriodField):
    """
    The net cash inflow (outflow) from discontinued investing activities over the designated time PeriodAsByte.
    """


class CashFromDiscontinuedOperatingCashFlowStatement(MultiPeriodField):
    """
    The net cash from (used in) all of the entity's discontinued operating activities, excluding those of continued operations, of the
    reporting entity.
    """


class ChangeInAccountPayableCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the account payables.
    """


class ChangeInTaxPayableCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the tax payables.
    """


class ChangeInAccruedExpenseCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the accrued expenses.
    """


class ChangeInAccruedInvestmentIncomeCashFlowStatement(MultiPeriodField):
    """
    The net change during the reporting period in investment income that has been earned but not yet received in cash.
    """


class ChangesInCashCashFlowStatement(MultiPeriodField):
    """
    The net change between the beginning and ending balance of cash and cash equivalents.
    """


class ChangeInDeferredAcquisitionCostsCashFlowStatement(MultiPeriodField):
    """
    The change of the unamortized portion as of the balance sheet date of capitalized costs that vary with and are primarily related to
    the acquisition of new and renewal insurance contracts.
    """


class ChangeInFederalFundsAndSecuritiesSoldForRepurchaseCashFlowStatement(MultiPeriodField):
    """
    The amount shown on the books that a bank with insufficient reserves borrows, at the federal funds rate, from another bank to
    meet its reserve requirements and the amount of securities that an institution sells and agrees to repurchase at a specified date for
    a specified price, net of any reductions or offsets.
    """


class ChangeInFundsWithheldCashFlowStatement(MultiPeriodField):
    """
    The net change during the reporting period associated with funds withheld.
    """


class ChangeInIncomeTaxPayableCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the income tax payables.
    """


class ChangeInInterestPayableCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the interest payable. Interest payable means carrying value as of the balance sheet
    date of interest payable on all forms of debt.
    """


class ChangeInInventoryCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the Inventories. Inventories represent merchandise bought for resale and supplies and
    raw materials purchased for use in revenue producing operations.
    """


class ChangeInLoansCashFlowStatement(MultiPeriodField):
    """
    The net change that a lender gives money or property to a borrower and the borrower agrees to return the property or repay the
    borrowed money, along with interest, at a predetermined date in the future.
    """


class ChangeInLossAndLossAdjustmentExpenseReservesCashFlowStatement(MultiPeriodField):
    """
    The net change during the reporting period in the reserve account established to account for expected but unspecified losses.
    """


class ChangeInPayableCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the payables.
    """


class ChangeInPayablesAndAccruedExpenseCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the payables and accrued expenses. Accrued expenses represent expenses incurred
    at the end of the reporting period but not yet paid; also called accrued liabilities. The accrued liability is shown under current
    liabilities in the balance sheet.
    """


class ChangeInPrepaidAssetsCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the prepaid assets.
    """


class ChangeInReceivablesCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the receivables. Receivables are amounts due to be paid to the company from clients
    and other.
    """


class ChangeInReinsuranceRecoverableOnPaidAndUnpaidLossesCashFlowStatement(MultiPeriodField):
    """
    The net change during the reporting period in the amount of benefits the ceding insurer expects to recover on insurance policies
    ceded to other insurance entities as of the balance sheet date for all guaranteed benefit types.
    """


class ChangeInRestrictedCashCashFlowStatement(MultiPeriodField):
    """
    The net cash inflow (outflow) for the net change associated with funds that are not available for withdrawal or use (such as funds
    held in escrow).
    """


class ChangeInTradingAccountSecuritiesCashFlowStatement(MultiPeriodField):
    """
    The net change during the reporting period associated with trading account assets. Trading account assets are bought and held
    principally for the purpose of selling them in the near term (thus held for only a short period of time). Unrealized holding gains and
    losses for trading securities are included in earnings.
    """


class ChangeInWorkingCapitalCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the working capital.  Working Capital is the amount left to the company to finance
    operations and expansion after current liabilities have been covered.
    """


class DeferredIncomeTaxCashFlowStatement(MultiPeriodField):
    """
    The component of income tax expense for the period representing the net change in the entities deferred tax assets and liabilities
    pertaining to continuing operations.
    """


class DeferredTaxCashFlowStatement(MultiPeriodField):
    """
    Future tax liability or asset, resulting from temporary differences between book (accounting) value of assets and liabilities, and their
    tax value. This arises due to differences between financial accounting for shareholders and tax accounting.
    """


class DepletionCashFlowStatement(MultiPeriodField):
    """
    Unlike depreciation and amortization, which mainly describe the deduction of expenses due to the aging of equipment and property,
    depletion is the actual physical reduction of natural resources by companies.   For example, coalmines, oil fields and other natural
    resources are depleted on company accounting statements. This reduction in the quantity of resources is meant to assist in
    accurately identifying the value of the asset on the balance sheet.
    """


class DepreciationCashFlowStatement(MultiPeriodField):
    """
    An expense recorded to allocate a tangible asset's cost over its useful life. Since it is a non-cash expense, it increases free cash
    flow while decreasing reported earnings.
    """


class DepreciationAndAmortizationCashFlowStatement(MultiPeriodField):
    """
    The current period expense charged against earnings on long-lived, physical assets used in the normal conduct of business and not
    intended for resale to allocate or recognize the cost of assets over their useful lives; or to record the reduction in book value of an
    intangible asset over the benefit period of such asset.
    """


class DepreciationAmortizationDepletionCashFlowStatement(MultiPeriodField):
    """
    It is a non cash charge that represents a reduction in the value of fixed assets due to wear, age or obsolescence. This figure also
    includes amortization of leased property, intangibles, and goodwill, and depletion. This non-cash item is an add-back to the cash
    flow statement.
    """


class EffectOfExchangeRateChangesCashFlowStatement(MultiPeriodField):
    """
    The effect of exchange rate changes on cash balances held in foreign currencies.
    """


class IncreaseDecreaseInDepositCashFlowStatement(MultiPeriodField):
    """
    The aggregate net change during the reporting period in moneys given as security, collateral, or margin deposits.
    """


class NetCommonStockIssuanceCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of common stock.
    """


class NetIssuancePaymentsOfDebtCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of debt.
    """


class NetLongTermDebtIssuanceCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of long term debt. Long term debt includes notes payable, bonds payable, mortgage
    loans, convertible debt, subordinated debt and other types of long term debt.
    """


class NetPreferredStockIssuanceCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of preferred stock.
    """


class NetShortTermDebtIssuanceCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of short term debt.
    """


class NetCashFromDiscontinuedOperationsCashFlowStatement(MultiPeriodField):
    """
    The net cash from (used in) all of the entity's discontinued operating activities, excluding those of continued operations, of the
    reporting entity.
    """


class NetForeignCurrencyExchangeGainLossCashFlowStatement(MultiPeriodField):
    """
    The aggregate amount of realized and unrealized gain or loss resulting from changes in exchange rates between currencies.
    (Excludes foreign currency transactions designated as hedges of net investment in a foreign entity and inter-company foreign
    currency transactions that are of a long-term nature, when the entities to the transaction are consolidated, combined, or accounted
    for by the equity method in the reporting entity's financial statements. For certain entities, primarily banks, which are dealers in
    foreign exchange, foreign currency transaction gains or losses, may be disclosed as dealer gains or losses.)
    """


class NetIncomeFromContinuingOperationsCashFlowStatement(MultiPeriodField):
    """
    Revenue less expenses and taxes from the entity's ongoing operations and before income (loss) from discontinued operations,
    extraordinary items, impact of changes in accounting principles, minority interest, and various other reconciling adjustments;
    represents the starting line for Operating Cash Flow.
    """


class PaymentForLoansCashFlowStatement(MultiPeriodField):
    """
    Payment from a bank or insurance company to the lender who lends money or property based on the agreement, along with
    interest, at a predetermined date in the future.
    """


class CommonStockPaymentsCashFlowStatement(MultiPeriodField):
    """
    The cash outflow to reacquire common stock during the PeriodAsByte.
    """


class PreferredStockPaymentsCashFlowStatement(MultiPeriodField):
    """
    The cash outflow to reacquire preferred stock during the PeriodAsByte.
    """


class LongTermDebtPaymentsCashFlowStatement(MultiPeriodField):
    """
    The cash outflow for debt initially having maturity due after one year or beyond the normal operating cycle, if longer.
    """


class ShortTermDebtPaymentsCashFlowStatement(MultiPeriodField):
    """
    The cash outflow for a borrowing having initial term of repayment within one year or the normal operating cycle, if longer.
    """


class ProceedsFromLoansCashFlowStatement(MultiPeriodField):
    """
    The cash inflow from borrowing money or property for a bank or insurance company.
    """


class ProceedsFromStockOptionExercisedCashFlowStatement(MultiPeriodField):
    """
    The cash inflow associated with the amount received from holders exercising their stock options.
    """


class CommonStockIssuanceCashFlowStatement(MultiPeriodField):
    """
    The cash inflow from offering common stock, which is the additional capital contribution to the entity during the PeriodAsByte.
    """


class LongTermDebtIssuanceCashFlowStatement(MultiPeriodField):
    """
    The cash inflow from a debt initially having maturity due after one year or beyond the operating cycle, if longer.
    """


class PreferredStockIssuanceCashFlowStatement(MultiPeriodField):
    """
    The cash inflow from offering preferred stock.
    """


class ShortTermDebtIssuanceCashFlowStatement(MultiPeriodField):
    """
    The cash inflow from a debt initially having maturity due within one year or the normal operating cycle, if longer.
    """


class NetProceedsPaymentForLoanCashFlowStatement(MultiPeriodField):
    """
    The net value of proceeds or payments of loans.
    """


class ProceedsPaymentInInterestBearingDepositsInBankCashFlowStatement(MultiPeriodField):
    """
    The net change on interest-bearing deposits in other financial institutions for relatively short periods of time including, for example,
    certificates of deposits.
    """


class PurchaseOfIntangiblesCashFlowStatement(MultiPeriodField):
    """
    The amount of capital outlays undertaken to increase, construct or improve intangible assets.
    """


class PurchaseOfInvestmentCashFlowStatement(MultiPeriodField):
    """
    All purchases of investments, including both long term and short term.
    """


class PurchaseOfPPECashFlowStatement(MultiPeriodField):
    """
    The amount of capital outlays undertaken to increase, construct or improve capital assets. This category includes property, plant
    equipment, furniture, fixed assets, buildings, and improvement.
    """


class PurchaseOfBusinessCashFlowStatement(MultiPeriodField):
    """
    All the purchases of business including business acquisitions, investment in subsidiary; investing in affiliated companies, and join
    venture.
    """


class NetBusinessPurchaseAndSaleCashFlowStatement(MultiPeriodField):
    """
    The net change between Purchases/Sales of Business.
    """


class NetIntangiblesPurchaseAndSaleCashFlowStatement(MultiPeriodField):
    """
    The net change between Purchases/Sales of Intangibles.
    """


class NetInvestmentPurchaseAndSaleCashFlowStatement(MultiPeriodField):
    """
    The net change between Purchases/Sales of Investments.
    """


class NetPPEPurchaseAndSaleCashFlowStatement(MultiPeriodField):
    """
    The net change between Purchases/Sales of PPE.
    """


class SaleOfBusinessCashFlowStatement(MultiPeriodField):
    """
    Proceeds received from selling a business including proceeds from a subsidiary, and proceeds from an affiliated company.
    """


class SaleOfIntangiblesCashFlowStatement(MultiPeriodField):
    """
    The amount of capital inflow from the sale of all kinds of intangible assets.
    """


class SaleOfInvestmentCashFlowStatement(MultiPeriodField):
    """
    Proceeds received from selling all kind of investments, including both long term and short term.
    """


class SaleOfPPECashFlowStatement(MultiPeriodField):
    """
    Proceeds from selling any fixed assets such as property, plant and equipment, which also includes retirement of equipment.
    """


class ChangesInAccountReceivablesCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the accounts receivables.
    """


class AmortizationOfFinancingCostsAndDiscountsCashFlowStatement(MultiPeriodField):
    """
    The component of interest expense representing the non-cash expenses charged against earnings in the period to allocate debt
    discount and premium, and the costs to issue debt and obtain financing over the related debt instruments. This item is usually only
    available for bank industry.
    """


class AmortizationOfSecuritiesCashFlowStatement(MultiPeriodField):
    """
    Represents amortization of the allocation of a lump sum amount to different time periods, particularly for securities, debt, loans,
    and other forms of financing. Does not include amortization, amortization of capital expenditure and intangible assets.
    """


class AssetImpairmentChargeCashFlowStatement(MultiPeriodField):
    """
    The charge against earnings resulting from the aggregate write down of all assets from their carrying value to their fair value.
    """


class ChangeInDividendPayableCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the dividend payables.
    """


class ChangeInDeferredChargesCashFlowStatement(MultiPeriodField):
    """
    The net change during the reporting period in the value of expenditures made during the current reporting period for benefits that
    will be received over a period of years. This item is usually only available for bank industry.
    """


class ChangeInOtherCurrentAssetsCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the Other Current Assets. This category typically includes prepayments, deferred
    charges, and amounts (other than trade accounts) due from parents and subsidiaries.
    """


class ChangeInOtherCurrentLiabilitiesCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the Other Current liabilities. Other Current liabilities is a balance sheet entry used by
    companies to group together current liabilities that are not assigned to common liabilities such as debt obligations or accounts
    payable.
    """


class ChangeInOtherWorkingCapitalCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the other working capital.
    """


class ChangeInUnearnedPremiumsCashFlowStatement(MultiPeriodField):
    """
    The change during the period in the unearned portion of premiums written, excluding the portion amortized into income. This item is
    usually only available for insurance industry.
    """


class CommonStockDividendPaidCashFlowStatement(MultiPeriodField):
    """
    The cash outflow from the distribution of an entity's earnings in the form of dividends to common shareholders.
    """


class EarningsLossesFromEquityInvestmentsCashFlowStatement(MultiPeriodField):
    """
    This item represents the entity's proportionate share for the period of the net income (loss) of its investee (such as unconsolidated
    subsidiaries and joint ventures) to which the equity method of accounting is applied. The amount typically reflects adjustments.
    """


class ExcessTaxBenefitFromStockBasedCompensationCashFlowStatement(MultiPeriodField):
    """
    Reductions in the entity's income taxes that arise when compensation cost (from non-qualified share-based compensation)
    recognized on the entities tax return exceeds compensation cost from share-based compensation recognized in financial
    statements. This element reduces net cash provided by operating activities.
    """


class GainLossOnInvestmentSecuritiesCashFlowStatement(MultiPeriodField):
    """
    This item represents the net total realized gain (loss) included in earnings for the period as a result of selling or holding marketable
    securities categorized as trading, available-for-sale, or held-to-maturity, including the unrealized holding gain or loss of held-to-
    maturity securities transferred to the trading security category and the cumulative unrealized gain or loss which was included in
    other comprehensive income (a separate component of shareholders' equity) for available-for-sale securities transferred to trading
    securities during the PeriodAsByte. Additionally, this item would include any losses recognized for other than temporary impairments of the
    subject investments in debt and equity securities.
    """


class GainLossOnSaleOfBusinessCashFlowStatement(MultiPeriodField):
    """
    The difference between the sale price or salvage price and the book value of an asset that was sold or retired during the reporting
    PeriodAsByte. This element refers to the gain (loss) and not to the cash proceeds of the business. This element is a non-cash adjustment
    to net income when calculating net cash generated by operating activities using the indirect method.
    """


class GainLossOnSaleOfPPECashFlowStatement(MultiPeriodField):
    """
    The difference between the sale price or salvage price and the book value of the property, plant and equipment that was sold or
    retired during the reporting PeriodAsByte. Includes the amount received from selling any fixed assets such as property, plant and
    equipment. Usually this section also includes any retirement of equipment. Such as Sale of business segments; Sale of credit and
    receivables; Property disposition; Proceeds from sale or disposition of business or investment; Decrease in excess of purchase price
    over acquired net assets; Abandoned project (expenditures) credit; Allowances for other funds during construction.
    """


class InterestCreditedOnPolicyholderDepositsCashFlowStatement(MultiPeriodField):
    """
    An expense reported in the income statement and needs to be removed from net income to arrive at cash provided by (used in)
    operations to the extent that such interest has not been paid. This item is usually only available for insurance industry.
    """


class CashFromDiscontinuedOperatingActivitiesCashFlowStatement(MultiPeriodField):
    """
    The net cash from (used in) all of the entity's discontinued operating activities, excluding those of continued operations, of the
    reporting entity.
    """


class OperatingGainsLossesCashFlowStatement(MultiPeriodField):
    """
    The gain or loss from the entity's ongoing operations.
    """


class NetOtherFinancingChargesCashFlowStatement(MultiPeriodField):
    """
    Miscellaneous charges incurred due to Financing activities.
    """


class NetOtherInvestingChangesCashFlowStatement(MultiPeriodField):
    """
    Miscellaneous charges incurred due to Investing activities.
    """


class OtherNonCashItemsCashFlowStatement(MultiPeriodField):
    """
    Items which adjusted back from net income but without real cash outflow or inflow.
    """


class PensionAndEmployeeBenefitExpenseCashFlowStatement(MultiPeriodField):
    """
    The amount of pension and other (such as medical, dental and life insurance) postretirement benefit costs recognized during the
    PeriodAsByte.
    """


class PreferredStockDividendPaidCashFlowStatement(MultiPeriodField):
    """
    Pay for the amount of dividends declared or paid in the period to preferred shareholders or the amount for which the obligation to
    pay them dividends rose in the PeriodAsByte.
    """


class ProceedsPaymentFederalFundsSoldAndSecuritiesPurchasedUnderAgreementToResellCashFlowStatement(MultiPeriodField):
    """
    The aggregate amount change of (1) the lending of excess federal funds to another commercial bank requiring such for its legal
    reserve requirements and (2) securities purchased under agreements to resell. This item is usually only available for bank industry.
    """


class ProvisionForLoanLeaseAndOtherLossesCashFlowStatement(MultiPeriodField):
    """
    The sum of the periodic provision charged to earnings, based on an assessment of uncollectible from the counterparty on account
    of loan, lease or other credit losses, to reduce these accounts to the amount that approximates their net realizable value. This item
    is usually only available for bank industry.
    """


class RealizedGainLossOnSaleOfLoansAndLeaseCashFlowStatement(MultiPeriodField):
    """
    The gains and losses included in earnings that represent the difference between the sale price and the carrying value of loans and
    leases that were sold during the reporting PeriodAsByte. This element refers to the gain (loss) and not to the cash proceeds of the sales.
    This element is a non-cash adjustment to net income when calculating net cash generated by operating activities using the indirect
    method. This item is usually only available for bank industry.
    """


class StockBasedCompensationCashFlowStatement(MultiPeriodField):
    """
    Value of stock issued during the period as a result of any share-based compensation plan other than an employee stock ownership
    plan (ESOP).
    """


class UnrealizedGainLossOnInvestmentSecuritiesCashFlowStatement(MultiPeriodField):
    """
    The increases (decreases) in the market value of unsold securities whose gains (losses) were included in earnings.
    """


class UnrealizedGainsLossesOnDerivativesCashFlowStatement(MultiPeriodField):
    """
    The gross gains and losses on derivatives. This item is usually only available for insurance industry.
    """


class AmortizationOfIntangiblesCashFlowStatement(MultiPeriodField):
    """
    The aggregate expense charged against earnings to allocate the cost of intangible assets (nonphysical assets not used in
    production) in a systematic and rational manner to the periods expected to benefit from such assets.
    """


class IncomeTaxPaidSupplementalDataCashFlowStatement(MultiPeriodField):
    """
    The amount of cash paid during the current period to foreign, federal state and local authorities as taxes on income.
    """


class InterestPaidSupplementalDataCashFlowStatement(MultiPeriodField):
    """
    The amount of cash paid during the current period for interest owed on money borrowed; including amount of interest capitalized.
    """


class IssuanceOfCapitalStockCashFlowStatement(MultiPeriodField):
    """
    The cash inflow from offering common stock, which is the additional capital contribution to the entity during the PeriodAsByte.
    """


class IssuanceOfDebtCashFlowStatement(MultiPeriodField):
    """
    The cash inflow due to an increase in long term debt.
    """


class RepaymentOfDebtCashFlowStatement(MultiPeriodField):
    """
    Payments to Settle Long Term Debt plus Payments to Settle Short Term Debt.
    """


class RepurchaseOfCapitalStockCashFlowStatement(MultiPeriodField):
    """
    Payments for Common Stock plus Payments for Preferred Stock.
    """


class FreeCashFlowCashFlowStatement(MultiPeriodField):
    """
    Cash Flow Operations minus Capital Expenditures.
    """


class DecreaseinInterestBearingDepositsinBankCashFlowStatement(MultiPeriodField):
    """
    The net change on interest-bearing deposits in other financial institutions for relatively short periods of time including, for example,
    certificates of deposits.
    """


class IncreaseinInterestBearingDepositsinBankCashFlowStatement(MultiPeriodField):
    """
    Increase in interest-bearing deposits in bank.
    """


class InterestReceivedCFOCashFlowStatement(MultiPeriodField):
    """
    Interest received by the company, in the Operating Cash Flow section.
    """


class InterestPaidCFOCashFlowStatement(MultiPeriodField):
    """
    Interest paid on loans, debt or borrowings, in the Operating Cash Flow section.
    """


class PurchaseofSubsidiariesCashFlowStatement(MultiPeriodField):
    """
    Purchase of subsidiaries or interest in subsidiaries (investments 51% and above).
    """


class PurchaseofJointVentureAssociateCashFlowStatement(MultiPeriodField):
    """
    Purchase of joint venture/associates (investment below 50%).
    """


class SaleofSubsidiariesCashFlowStatement(MultiPeriodField):
    """
    Cash inflow from the disposal of any subsidiaries.
    """


class SaleofJointVentureAssociateCashFlowStatement(MultiPeriodField):
    """
    Cash inflow from the disposal of joint venture/associates (investment below 50%).
    """


class IncreaseDecreaseinLeaseFinancingCashFlowStatement(MultiPeriodField):
    """
    Change in cash flow resulting from increase/decrease in lease financing.
    """


class IncreaseinLeaseFinancingCashFlowStatement(MultiPeriodField):
    """
    The cash inflow from increase in lease financing.
    """


class RepaymentinLeaseFinancingCashFlowStatement(MultiPeriodField):
    """
    The cash outflow to repay lease financing during the PeriodAsByte.
    """


class ShareofAssociatesCashFlowStatement(MultiPeriodField):
    """
    A non-cash adjustment for share of associates' income in respect of operating activities.
    """


class ProfitonDisposalsCashFlowStatement(MultiPeriodField):
    """
    The difference between the sale price or salvage price and the book value of an asset that was sold or retired during the reporting
    PeriodAsByte.
    """


class ReorganizationOtherCostsCashFlowStatement(MultiPeriodField):
    """
    A non-cash adjustment relating to restructuring costs.
    """


class NetOutwardLoansCashFlowStatement(MultiPeriodField):
    """
    Adjustments due to net loans to/from outsiders in the Investing Cash Flow section.
    """


class IssueExpensesCashFlowStatement(MultiPeriodField):
    """
    Cost associated with issuance of debt/equity capital in the Financing Cash Flow section.
    """


class ChangeinDepositsbyBanksandCustomersCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the deposits by banks and customers.
    """


class CashFlowsfromusedinOperatingActivitiesDirectCashFlowStatement(MultiPeriodField):
    """
    The net cash from (used in) all of the entity's operating activities, including those of discontinued operations, of the reporting entity
    under the direct method.
    """


class ClassesofCashReceiptsfromOperatingActivitiesCashFlowStatement(MultiPeriodField):
    """
    Sum of total cash receipts in the direct cash flow.
    """


class OtherCashReceiptsfromOperatingActivitiesCashFlowStatement(MultiPeriodField):
    """
    Other cash receipts for the direct cash flow.
    """


class ClassesofCashPaymentsCashFlowStatement(MultiPeriodField):
    """
    Sum of total cash payment in the direct cash flow.
    """


class PaymentstoSuppliersforGoodsandServicesCashFlowStatement(MultiPeriodField):
    """
    Cash paid to suppliers when purchasing goods or services by the company, in the direct cash flow.
    """


class PaymentsonBehalfofEmployeesCashFlowStatement(MultiPeriodField):
    """
    Cash paid in a form of salaries or other benefits to employees of the company, in the direct cash flow.
    """


class OtherCashPaymentsfromOperatingActivitiesCashFlowStatement(MultiPeriodField):
    """
    Other cash payments for the direct cash flow.
    """


class DividendsPaidDirectCashFlowStatement(MultiPeriodField):
    """
    Dividend paid to the investors, for the direct cash flow.
    """


class DividendsReceivedDirectCashFlowStatement(MultiPeriodField):
    """
    Dividend received on the investment, for the direct cash flow.
    """


class InterestPaidDirectCashFlowStatement(MultiPeriodField):
    """
    Interest paid on loans, debt or borrowings, in the direct cash flow.
    """


class InterestReceivedDirectCashFlowStatement(MultiPeriodField):
    """
    Interest received by the company, in the direct cash flow.
    """


class TaxesRefundPaidDirectCashFlowStatement(MultiPeriodField):
    """
    Tax paid/refund related to operating activities, for the direct cash flow.
    """


class TotalAdjustmentsforNonCashItemsCashFlowStatement(MultiPeriodField):
    """
    Sum of all adjustments back from net income but without real cash outflow or inflow.
    """


class ImpairmentLossReversalRecognizedinProfitorLossCashFlowStatement(MultiPeriodField):
    """
    The difference between the future net cash flows expected to be received from the asset and its book value, recognized in the
    Income Statement.
    """


class DividendPaidCFOCashFlowStatement(MultiPeriodField):
    """
    Dividend paid to the investors, in the Operating Cash Flow section.
    """


class DividendReceivedCFOCashFlowStatement(MultiPeriodField):
    """
    Dividend received on investment, in the Operating Cash Flow section.
    """


class TaxesRefundPaidCashFlowStatement(MultiPeriodField):
    """
    Total tax paid or received on operating activities.
    """


class OtherOperatingInflowsOutflowsofCashCashFlowStatement(MultiPeriodField):
    """
    Any other cash inflows or outflows in the Operating Cash Flow section, not accounted for in the other specified items.
    """


class CashAdvancesandLoansMadetoOtherPartiesCashFlowStatement(MultiPeriodField):
    """
    Cash outlay for cash advances and loans made to other parties.
    """


class CashReceiptsfromRepaymentofAdvancesandLoansMadetoOtherPartiesCashFlowStatement(MultiPeriodField):
    """
    Cash received from the repayment of advances and loans made to other parties, in the Investing Cash Flow section.
    """


class DividendsReceivedCFICashFlowStatement(MultiPeriodField):
    """
    Dividend received on investment, in the Investing Cash Flow section.
    """


class InterestReceivedCFICashFlowStatement(MultiPeriodField):
    """
    Interest received by the company, in the Investing Cash Flow section.
    """


class InterestPaidCFFCashFlowStatement(MultiPeriodField):
    """
    Interest paid on loans, debt or borrowings, in the Financing Cash Flow section.
    """


class ChangeinAccruedIncomeCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods in the amount of outstanding money owed by a customer for goods or services provided
    by the company.
    """


class ChangeinFinancialAssetsCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the financial assets.
    """


class ChangeinAdvancesfromCentralBanksCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the advances from central banks.
    """


class ChangeinFinancialLiabilitiesCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the financial liabilities.
    """


class ChangeinInsuranceContractAssetsCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the contract assets.
    """


class ChangeinReinsuranceReceivablesCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the reinsurance receivable.
    """


class ChangeinDeferredAcquisitionCostsNetCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the deferred acquisition costs.
    """


class ChangeinInsuranceFundsCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the insurance funds.
    """


class ChangeinInvestmentContractLiabilitiesCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the investment contract liabilities.
    """


class ChangeinInsuranceContractLiabilitiesCashFlowStatement(MultiPeriodField):
    """
    The increase or decrease between periods of the insurance contract liabilities.
    """


class ProvisionandWriteOffofAssetsCashFlowStatement(MultiPeriodField):
    """
    A non-cash adjustment for total provision and write off on assets &amp; liabilities.
    """


class ReceiptsfromCustomersCashFlowStatement(MultiPeriodField):
    """
    Payment received from customers in the Direct Cash Flow.
    """


class ReceiptsfromGovernmentGrantsCashFlowStatement(MultiPeriodField):
    """
    Cash received from governments in the form of grants in the Direct Cash Flow.
    """


class MinorityInterestCashFlowStatement(MultiPeriodField):
    """
    Amount of net income (loss) for the period allocated to non-controlling shareholders, partners, or other equity holders in one or
    more of the entities included.
    """


class CapExReportedCashFlowStatement(MultiPeriodField):
    """
    Capital expenditure, capitalized software development cost, maintenance capital expenditure, etc. as reported by the company.
    """


class CashReceiptsfromTaxRefundsCashFlowStatement(MultiPeriodField):
    """
    Cash received as refunds from tax authorities in operating cash flow, using the direct method
    """


class CashReceiptsfromDepositsbyBanksandCustomersCashFlowStatement(MultiPeriodField):
    """
    Cash received from banks and customer deposits in operating cash flow, using the direct method. This item is usually only available
    for bank industry
    """


class CashReceiptsfromLoansCashFlowStatement(MultiPeriodField):
    """
    Cash received from loans in operating cash flow, using the direct method. This item is usually only available for bank industry
    """


class CashReceiptsfromSecuritiesRelatedActivitiesCashFlowStatement(MultiPeriodField):
    """
    Cash received from the trading of securities in operating cash flow, using the direct method. This item is usually only available for
    bank and insurance industries
    """


class CashReceiptsfromFeesandCommissionsCashFlowStatement(MultiPeriodField):
    """
    Cash received from agency fees and commissions in operating cash flow, using the direct method. This item is usually available for
    bank and insurance industries
    """


class CashPaymentsforDepositsbyBanksandCustomersCashFlowStatement(MultiPeriodField):
    """
    Cash paid for deposits by banks and customers in operating cash flow, using the direct method. This item is usually only available
    for bank industry
    """


class CashPaymentsforLoansCashFlowStatement(MultiPeriodField):
    """
    Cash paid for loans in operating cash flow, using the direct method. This item is usually only available for bank industry
    """


class InterestandCommissionPaidCashFlowStatement(MultiPeriodField):
    """
    Cash paid for interest and commission in operating cash flow, using the direct method
    """


class AllTaxesPaidCashFlowStatement(MultiPeriodField):
    """
    Cash paid to tax authorities in operating cash flow, using the direct method
    """


class CashReceivedfromInsuranceActivitiesCashFlowStatement(MultiPeriodField):
    """
    Cash received from insurance activities in operating cash flow, using the direct method. This item is usually only available for
    insurance industry
    """


class PremiumReceivedCashFlowStatement(MultiPeriodField):
    """
    Cash received from premium income in operating cash flow, using the direct method. This item is usually only available for
    insurance industry
    """


class ReinsuranceandOtherRecoveriesReceivedCashFlowStatement(MultiPeriodField):
    """
    Cash received from reinsurance income or other recoveries income in operating cash flow, using the direct method. This item is
    usually only available for insurance industry
    """


class PolicyholderDepositInvestmentReceivedCashFlowStatement(MultiPeriodField):
    """
    Cash received from policyholder deposit investment activities in operating cash flow, using the direct method. This item is usually
    only available for insurance industry
    """


class CashPaidforInsuranceActivitiesCashFlowStatement(MultiPeriodField):
    """
    Cash paid out for insurance activities during the period in operating cash flow, using the direct method. This item is usually only
    available for insurance industry
    """


class ClaimsPaidCashFlowStatement(MultiPeriodField):
    """
    Cash paid out for claims by a insurance company during the period in operating cash flow, using the direct method. This item is
    usually only available for insurance industry
    """


class CommissionPaidCashFlowStatement(MultiPeriodField):
    """
    Cash paid for commissions in operating cash flow, using the direct method
    """


class CashPaidtoReinsurersCashFlowStatement(MultiPeriodField):
    """
    Cash paid out to reinsurers in operating cash flow, using the direct method. This item is usually only available for insurance industry
    """


class OtherUnderwritingExpensesPaidCashFlowStatement(MultiPeriodField):
    """
    Cash paid out for underwriting expenses, such as the acquisition of new and renewal insurance contracts, in operating cash flow,
    using the direct method. This item is usually only available for insurance industry
    """


class CashDividendsForMinoritiesCashFlowStatement(MultiPeriodField):
    """
    Cash Distribution of earnings to Minority Stockholders.
    """


class CashGeneratedfromOperatingActivitiesCashFlowStatement(MultiPeriodField):
    """
    The net cash from an entity's operating activities before real cash inflow or outflow for Dividend, Interest, Tax, or other unclassified
    operating activities.
    """


class FundFromOperationCashFlowStatement(MultiPeriodField):
    """
    Funds from operations; populated only for real estate investment trusts (REITs), defined as the sum of net income, gain/loss
    (realized and unrealized) on investment securities, asset impairment charge, depreciation and amortization and gain/ loss on the
    sale of business and property plant and equipment.
    """


class NetInvestmentPropertiesPurchaseAndSaleCashFlowStatement(MultiPeriodField):
    """
    Net increase or decrease in cash due to purchases or sales of investment properties during the accounting PeriodAsByte.
    """


class PurchaseOfInvestmentPropertiesCashFlowStatement(MultiPeriodField):
    """
    Cash outflow for purchases of investment properties during the accounting PeriodAsByte.
    """


class SaleOfInvestmentPropertiesCashFlowStatement(MultiPeriodField):
    """
    Cash inflow from sale of investment properties during the accounting PeriodAsByte.
    """


class OtherCashAdjustIncludedIntoChangeinCashCashFlowStatement(MultiPeriodField):
    """
    Other cash adjustments included in change in cash not categorized above.
    """


class OtherCashAdjustExcludeFromChangeinCashCashFlowStatement(MultiPeriodField):
    """
    Other changes to cash and cash equivalents during the accounting PeriodAsByte.
    """


class ChangeinCashSupplementalAsReportedCashFlowStatement(MultiPeriodField):
    """
    The change in cash flow from the previous period to the current, as reported by the company, may be the same or not the same as
    Morningstar's standardized definition. It is a supplemental value which would be reported outside consolidated statements.
    """


class TotalRiskBasedCapital(MultiPeriodField):
    """
    The sum of Tier 1 and Tier 2 Capital. Tier 1 capital consists of common shareholders equity, perpetual preferred shareholders equity
    with non-cumulative dividends, retained earnings, and minority interests in the equity accounts of consolidated subsidiaries. Tier 2
    capital consists of subordinated debt, intermediate-term preferred stock, cumulative and long-term preferred stock, and a portion of
    a bank's allowance for loan and lease losses.
    """


class BasicContinuousOperations(MultiPeriodField):
    """
    Basic EPS from Continuing Operations is the earnings from continuing operations reported by the company divided by the weighted
    average number of common shares outstanding.
    """


class BasicDiscontinuousOperations(MultiPeriodField):
    """
    Basic EPS from Discontinued Operations is the earnings from discontinued operations reported by the company divided by the
    weighted average number of common shares outstanding. This only includes gain or loss from discontinued operations.
    """


class BasicExtraordinary(MultiPeriodField):
    """
    Basic EPS from the Extraordinary Gains/Losses is the earnings attributable to the gains or losses (during the reporting period) from
    extraordinary items divided by the weighted average number of common shares outstanding.
    """


class BasicAccountingChange(MultiPeriodField):
    """
    Basic EPS from the Cumulative Effect of Accounting Change is the earnings attributable to the accounting change (during the
    reporting period) divided by the weighted average number of common shares outstanding.
    """


class BasicEPS(MultiPeriodField):
    """
    Basic EPS is the bottom line net income divided by the weighted average number of common shares outstanding.
    """


class DilutedContinuousOperations(MultiPeriodField):
    """
    Diluted EPS from Continuing Operations is the earnings from continuing operations divided by the common shares outstanding
    adjusted for the assumed conversion of all potentially dilutive securities.  Securities having a dilutive effect may include convertible
    debentures, warrants, options, and convertible preferred stock.
    """


class DilutedDiscontinuousOperations(MultiPeriodField):
    """
    Diluted EPS from Discontinued Operations is the earnings from discontinued operations divided by the common shares outstanding
    adjusted for the assumed conversion of all potentially dilutive securities. Securities having a dilutive effect may include convertible
    debentures, warrants, options, and convertible preferred stock. This only includes gain or loss from discontinued operations.
    """


class DilutedExtraordinary(MultiPeriodField):
    """
    Diluted EPS from Extraordinary Gain/Losses is the gain or loss from extraordinary items divided by the common shares outstanding
    adjusted for the assumed conversion of all potentially dilutive securities. Securities having a dilutive effect may include convertible
    debentures, warrants, options, and convertible preferred stock.
    """


class DilutedAccountingChange(MultiPeriodField):
    """
    Diluted EPS from Cumulative Effect Accounting Changes is the earnings from accounting changes (in the reporting period) divided
    by the common shares outstanding adjusted for the assumed conversion of all potentially dilutive securities. Securities having a
    dilutive effect may include convertible debentures, warrants, options, and convertible preferred stock.
    """


class DilutedEPS(MultiPeriodField):
    """
    Diluted EPS is the bottom line net income divided by the common shares outstanding adjusted for the assumed conversion of all
    potentially dilutive securities. Securities having a dilutive effect may include convertible debentures, warrants, options, and
    convertible preferred stock. This value will be derived when not reported for the fourth quarter and will be less than or equal to
    Basic EPS.
    """


class BasicAverageShares(MultiPeriodField):
    """
    The shares outstanding used to calculate Basic EPS, which is the weighted average common share outstanding through the whole
    accounting PeriodAsByte.  Note: If Basic Average Shares are not presented by the firm in the Income Statement, this data point will be
    null.
    """


class DilutedAverageShares(MultiPeriodField):
    """
    The shares outstanding used to calculate the diluted EPS, assuming the conversion of all convertible securities and the exercise of
    warrants or stock options. It is the weighted average diluted share outstanding through the whole accounting PeriodAsByte.  Note: If
    Diluted Average Shares are not presented by the firm in the Income Statement and Basic Average Shares are presented, Diluted
    Average Shares will equal Basic Average Shares.  However, if neither value is presented by the firm, Diluted Average Shares will be
    null.
    """


class DividendPerShare(MultiPeriodField):
    """
    The amount of dividend that a stockholder will receive for each share of stock held. It can be calculated by taking the total amount
    of dividends paid and dividing it by the total shares outstanding. Dividend per share = total dividend payment/total number of
    outstanding shares
    """


class BasicEPSOtherGainsLosses(MultiPeriodField):
    """
    Basic EPS from the Other Gains/Losses is the earnings attributable to the other gains/losses (during the reporting period) divided by
    the weighted average number of common shares outstanding.
    """


class ContinuingAndDiscontinuedBasicEPS(MultiPeriodField):
    """
    Basic EPS from Continuing Operations plus Basic EPS from Discontinued Operations.
    """


class TaxLossCarryforwardBasicEPS(MultiPeriodField):
    """
    The earnings attributable to the tax loss carry forward (during the reporting period).
    """


class DilutedEPSOtherGainsLosses(MultiPeriodField):
    """
    The earnings from gains and losses (in the reporting period) divided by the common shares outstanding adjusted for the assumed
    conversion of all potentially dilutive securities. Securities having a dilutive effect may include convertible debentures, warrants,
    options, convertible preferred stock, etc.
    """


class ContinuingAndDiscontinuedDilutedEPS(MultiPeriodField):
    """
    Diluted EPS from Continuing Operations plus Diluted EPS from Discontinued Operations.
    """


class TaxLossCarryforwardDilutedEPS(MultiPeriodField):
    """
    The earnings from any tax loss carry forward (in the reporting period).
    """


class NormalizedBasicEPS(MultiPeriodField):
    """
    The basic normalized earnings per share. Normalized EPS removes onetime and unusual items from EPS, to provide investors with a
    more accurate measure of the company's true earnings. Normalized Earnings / Basic Weighted Average Shares Outstanding.
    """


class NormalizedDilutedEPS(MultiPeriodField):
    """
    The diluted normalized earnings per share. Normalized EPS removes onetime and unusual items from EPS, to provide investors with
    a more accurate measure of the company's true earnings. Normalized Earnings / Diluted Weighted Average Shares Outstanding.
    """


class TotalDividendPerShare(MultiPeriodField):
    """
    Total Dividend Per Share is cash dividends and special cash dividends paid per share over a certain period of time.
    """


class ReportedNormalizedBasicEPS(MultiPeriodField):
    """
    Normalized Basic EPS as reported by the company in the financial statements.
    """


class ReportedNormalizedDilutedEPS(MultiPeriodField):
    """
    Normalized Diluted EPS as reported by the company in the financial statements.
    """


class DividendCoverageRatio(MultiPeriodField):
    """
    Reflects a firm's capacity to pay a dividend, and is defined as Earnings Per Share / Dividend Per Share
    """


class RevenueGrowth(MultiPeriodField):
    """
    The growth in the company's revenue on a percentage basis. Morningstar calculates the growth percentage based on the
    underlying revenue data reported in the Income Statement within the company filings or reports.
    """


class OperationIncomeGrowth(MultiPeriodField):
    """
    The growth in the company's operating income on a percentage basis. Morningstar calculates the growth percentage based on the
    underlying operating income data reported in the Income Statement within the company filings or reports.
    """


class NetIncomeGrowth(MultiPeriodField):
    """
    The growth in the company's net income on a percentage basis. Morningstar calculates the growth percentage based on the
    underlying net income data reported in the Income Statement within the company filings or reports.
    """


class NetIncomeContOpsGrowth(MultiPeriodField):
    """
    The growth in the company's net income from continuing operations on a percentage basis. Morningstar calculates the growth
    percentage based on the underlying net income from continuing operations data reported in the Income Statement within the
    company filings or reports. This figure represents the rate of net income growth for parts of the business that will continue to
    generate revenue in the future.
    """


class CFOGrowth(MultiPeriodField):
    """
    The growth in the company's cash flow from operations on a percentage basis. Morningstar calculates the growth percentage
    based on the underlying cash flow from operations data reported in the Cash Flow Statement within the company filings or reports.
    """


class FCFGrowth(MultiPeriodField):
    """
    The growth in the company's free cash flow on a percentage basis. Morningstar calculates the growth percentage based on the
    underlying cash flow from operations and capital expenditures data reported in the Cash Flow Statement within the company filings
    or reports:   Free Cash Flow = Cash flow from operations - Capital Expenditures.
    """


class OperationRevenueGrowth3MonthAvg(MultiPeriodField):
    """
    The growth in the company's operating revenue on a percentage basis. Morningstar calculates the growth percentage based on
    the underlying operating revenue data reported in the Income Statement within the company filings or reports.
    """


class GrossMargin(MultiPeriodField):
    """
    Refers to the ratio of gross profit to revenue. Morningstar calculates the ratio by using the underlying data reported in the company
    filings or reports:   (Revenue - Cost of Goods Sold) / Revenue.
    """


class OperationMargin(MultiPeriodField):
    """
    Refers to the ratio of operating income to revenue. Morningstar calculates the ratio by using the underlying data reported in the
    company filings or reports:   Operating Income / Revenue.
    """


class PretaxMargin(MultiPeriodField):
    """
    Refers to the ratio of pretax income to revenue. Morningstar calculates the ratio by using the underlying data reported in the
    company filings or reports:   Pretax Income / Revenue.
    """


class NetMargin(MultiPeriodField):
    """
    Refers to the ratio of net income to revenue. Morningstar calculates the ratio by using the underlying data reported in the company
    filings or reports:   Net Income / Revenue.
    """


class TaxRate(MultiPeriodField):
    """
    Refers to the ratio of tax provision to pretax income. Morningstar calculates the ratio by using the underlying data reported in the
    company filings or reports:   Tax Provision / Pretax Income.
    [Note: Valid only when positive pretax income, and positive tax expense (not tax benefit)]
    """


class EBITMargin(MultiPeriodField):
    """
    Refers to the ratio of earnings before interest and taxes to revenue. Morningstar calculates the ratio by using the underlying data
    reported in the company filings or reports:   EBIT / Revenue.
    """


class EBITDAMargin(MultiPeriodField):
    """
    Refers to the ratio of earnings before interest, taxes and depreciation and amortization to revenue. Morningstar calculates the ratio
    by using the underlying data reported in the company filings or reports:   EBITDA / Revenue.
    """


class SalesPerEmployee(MultiPeriodField):
    """
    Refers to the ratio of Revenue to Employees. Morningstar calculates the ratio by using the underlying data reported in the company
    filings or reports:     Revenue / Employee Number.
    """


class CurrentRatio(MultiPeriodField):
    """
    Refers to the ratio of Current Assets to Current Liabilities. Morningstar calculates the ratio by using the underlying data reported in
    the Balance Sheet within the company filings or reports:     Current Assets / Current Liabilities.
    """


class QuickRatio(MultiPeriodField):
    """
    Refers to the ratio of liquid assets to Current Liabilities. Morningstar calculates the ratio by using the underlying data reported in the
    Balance Sheet within the company filings or reports:(Cash, Cash Equivalents, and Short Term Investments + Receivables ) /
    Current Liabilities.
    """


class LongTermDebtTotalCapitalRatio(MultiPeriodField):
    """
    Refers to the ratio of Long Term Debt to Total Capital. Morningstar calculates the ratio by using the underlying data reported in the
    Balance Sheet within the company filings or reports:    Long-Term Debt And Capital Lease Obligation / (Long-Term Debt And Capital
    Lease Obligation + Total Shareholder's Equity)
    """


class InterestCoverage(MultiPeriodField):
    """
    Refers to the ratio of EBIT to Interest Expense. Morningstar calculates the ratio by using the underlying data reported in the Income
    Statement within the company filings or reports:    EBIT / Interest Expense.
    """


class LongTermDebtEquityRatio(MultiPeriodField):
    """
    Refers to the ratio of Long Term Debt to Common Equity. Morningstar calculates the ratio by using the underlying data reported in
    the Balance Sheet within the company filings or reports:    Long-Term Debt And Capital Lease Obligation / Common Equity.
    [Note: Common Equity = Total Shareholder's Equity - Preferred Stock]
    """


class FinancialLeverage(MultiPeriodField):
    """
    Refers to the ratio of Total Assets to Common Equity. Morningstar calculates the ratio by using the underlying data reported in the
    Balance Sheet within the company filings or reports:    Total Assets / Common Equity.   [Note: Common Equity = Total
    Shareholder's Equity - Preferred Stock]
    """


class TotalDebtEquityRatio(MultiPeriodField):
    """
    Refers to the ratio of Total Debt to Common Equity. Morningstar calculates the ratio by using the underlying data reported in the
    Balance Sheet within the company filings or reports: (Current Debt And Current Capital Lease Obligation + Long-Term Debt And
    Long-Term Capital Lease Obligation / Common Equity.   [Note: Common Equity = Total Shareholder's Equity - Preferred Stock]
    """


class NormalizedNetProfitMargin(MultiPeriodField):
    """
    Normalized Income / Total Revenue. A measure of profitability of the company calculated by finding Normalized Net Profit as a
    percentage of Total Revenues.
    """


class DaysInSales(MultiPeriodField):
    """
    365 / Receivable Turnover
    """


class DaysInInventory(MultiPeriodField):
    """
    365 / Inventory turnover
    """


class DaysInPayment(MultiPeriodField):
    """
    365 / Payable turnover
    """


class CashConversionCycle(MultiPeriodField):
    """
    Days In Inventory + Days In Sales - Days In Payment
    """


class ReceivableTurnover(MultiPeriodField):
    """
    Revenue / Average Accounts Receivables
    """


class InventoryTurnover(MultiPeriodField):
    """
    Cost Of Goods Sold / Average Inventory
    """


class PaymentTurnover(MultiPeriodField):
    """
    Cost of Goods Sold / Average Accounts Payables
    """


class FixAssetsTuronver(MultiPeriodField):
    """
    Revenue / Average PP&amp;E
    """


class AssetsTurnover(MultiPeriodField):
    """
    Revenue / Average Total Assets
    """


class ROE(MultiPeriodField):
    """
    Net Income / Average Total Common Equity
    """


class ROA(MultiPeriodField):
    """
    Net Income / Average Total Assets
    """


class ROIC(MultiPeriodField):
    """
    Net Income / (Total Equity + Long-term Debt and Capital Lease Obligation + Short-term Debt and Capital Lease Obligation)
    """


class FCFSalesRatio(MultiPeriodField):
    """
    Free Cash flow / Revenue
    """


class FCFNetIncomeRatio(MultiPeriodField):
    """
    Free Cash Flow / Net Income
    """


class CapExSalesRatio(MultiPeriodField):
    """
    Capital Expenditure / Revenue
    """


class DebttoAssets(MultiPeriodField):
    """
    This is a leverage ratio used to determine how much debt (a sum of long term and current portion of debt) a company has on its
    balance sheet relative to total assets. This ratio examines the percent of the company that is financed by debt.
    """


class CommonEquityToAssets(MultiPeriodField):
    """
    This is a financial ratio of common stock equity to total assets that indicates the relative proportion of equity used to finance a
    company's assets.
    """


class CapitalExpenditureAnnual5YrGrowth(MultiPeriodField):
    """
    This is the compound annual growth rate of the company's capital spending over the last 5 years. Capital Spending is the sum of
    the Capital Expenditure items found in the Statement of Cash Flows.
    """


class GrossProfitAnnual5YrGrowth(MultiPeriodField):
    """
    This is the compound annual growth rate of the company's Gross Profit over the last 5 years.
    """


class GrossMargin5YrAvg(MultiPeriodField):
    """
    This is the simple average of the company's Annual Gross Margin over the last 5 years. Gross Margin is Total Revenue minus Cost
    of Goods Sold divided by Total Revenue and is expressed as a percentage.
    """


class PostTaxMargin5YrAvg(MultiPeriodField):
    """
    This is the simple average of the company's Annual Post Tax Margin over the last 5 years. Post tax margin is Post tax divided by
    total revenue for the same PeriodAsByte.
    """


class PreTaxMargin5YrAvg(MultiPeriodField):
    """
    This is the simple average of the company's Annual Pre Tax Margin over the last 5 years. Pre tax margin is Pre tax divided by total
    revenue for the same PeriodAsByte.
    """


class ProfitMargin5YrAvg(MultiPeriodField):
    """
    This is the simple average of the company's Annual Net Profit Margin over the last 5 years. Net profit margin is post tax income
    divided by total revenue for the same PeriodAsByte.
    """


class ROE5YrAvg(MultiPeriodField):
    """
    This is the simple average of the company's ROE over the last 5 years. Return on equity reveals how much profit a company has
    earned in comparison to the total amount of shareholder equity found on the balance sheet.
    """


class ROA5YrAvg(MultiPeriodField):
    """
    This is the simple average of the company's ROA over the last 5 years. Return on asset is calculated by dividing a company's annual
    earnings by its average total assets.
    """


class AVG5YrsROIC(MultiPeriodField):
    """
    This is the simple average of the company's ROIC over the last 5 years. Return on invested capital is calculated by taking net
    operating profit after taxes and dividends and dividing by the total amount of capital invested and expressing the result as a
    percentage.
    """


class NormalizedROIC(MultiPeriodField):
    """
    [Normalized Income + (Interest Expense * (1-Tax Rate))]  / Invested Capital
    """


class RegressionGrowthOperatingRevenue5Years(MultiPeriodField):
    """
    The five-year growth rate of operating revenue, calculated using regression analysis.
    """


class CashRatio(MultiPeriodField):
    """
    Indicates a company's short-term liquidity, defined as short term liquid investments (cash, cash equivalents, short term
    investments) divided by current liabilities.
    """


class CashtoTotalAssets(MultiPeriodField):
    """
    Represents the percentage of a company's total assets is in cash.
    """


class CapitalExpendituretoEBITDA(MultiPeriodField):
    """
    Measures the amount a company is investing in its business relative to EBITDA generated in a given PeriodAsByte.
    """


class FCFtoCFO(MultiPeriodField):
    """
    Indicates the percentage of a company's operating cash flow is free to be invested in its business after capital expenditures.
    """


class StockholdersEquityGrowth(MultiPeriodField):
    """
    The growth in the stockholder's equity on a percentage basis. Morningstar calculates the growth percentage based on the residual
    interest in the assets of the enterprise that remains after deducting its liabilities reported in the Balance Sheet within the company
    filings or reports.
    """


class TotalAssetsGrowth(MultiPeriodField):
    """
    The growth in the total assets on a percentage basis. Morningstar calculates the growth percentage based on the total assets
    reported in the Balance Sheet within the company filings or reports.
    """


class TotalLiabilitiesGrowth(MultiPeriodField):
    """
    The growth in the total liabilities on a percentage basis. Morningstar calculates the growth percentage based on the total liabilities
    reported in the Balance Sheet within the company filings or reports.
    """


class TotalDebtEquityRatioGrowth(MultiPeriodField):
    """
    The growth in the company's total debt to equity ratio on a percentage basis. Morningstar calculates the growth percentage based
    on the total debt divided by the shareholder's equity reported in the Balance Sheet within the company filings or reports.
    """


class CashRatioGrowth(MultiPeriodField):
    """
    The growth in the company's cash ratio on a percentage basis. Morningstar calculates the growth percentage based on the short
    term liquid investments (cash, cash equivalents, short term investments) divided by current liabilities reported in the Balance Sheet
    within the company filings or reports.
    """


class EBITDAGrowth(MultiPeriodField):
    """
    The growth in the company's EBITDA on a percentage basis. Morningstar calculates the growth percentage based on the earnings
    minus expenses (excluding interest, tax, depreciation, and amortization expenses) reported in the Financial Statements within the
    company filings or reports.
    """


class CashFlowfromFinancingGrowth(MultiPeriodField):
    """
    The growth in the company's cash flows from financing on a percentage basis. Morningstar calculates the growth percentage
    based on the financing cash flows reported in the Cash Flow Statement within the company filings or reports.
    """


class CashFlowfromInvestingGrowth(MultiPeriodField):
    """
    The growth in the company's cash flows from investing on a percentage basis. Morningstar calculates the growth percentage
    based on the cash flows from investing reported in the Cash Flow Statement within the company filings or reports.
    """


class CapExGrowth(MultiPeriodField):
    """
    The growth in the company's capital expenditures on a percentage basis. Morningstar calculates the growth percentage based on
    the capital expenditures reported in the Cash Flow Statement within the company filings or reports.
    """


class CurrentRatioGrowth(MultiPeriodField):
    """
    The growth in the company's current ratio on a percentage basis. Morningstar calculates the growth percentage based on the
    current assets divided by current liabilities reported in the Balance Sheet within the company filings or reports.
    """


class WorkingCapitalTurnoverRatio(MultiPeriodField):
    """
    Total revenue / working capital (current assets minus current liabilities)
    """


class NetIncomePerEmployee(MultiPeriodField):
    """
    Refers to the ratio of Net Income to Employees. Morningstar calculates the ratio by using the underlying data reported in the
    company filings or reports:     Net Income / Employee Number.
    """


class SolvencyRatio(MultiPeriodField):
    """
    Measure of whether a company's cash flow is sufficient to meet its short-term and long-term debt requirements. The lower this
    ratio is, the greater the probability that the company will be in financial distress. Net Income + Depreciation, Depletion and
    Amortization/ average of annual Total Liabilities over the most recent two periods.
    """


class ExpenseRatio(MultiPeriodField):
    """
    A measure of operating performance for Insurance companies, as it shows the relationship between the premiums earned and
    administrative expenses related to claims such as fees and commissions. A number of 1 or lower is preferred, as this means the
    premiums exceed the expenses. Calculated as: (Deferred Policy Acquisition Amortization Expense+Fees and Commission
    Expense+Other Underwriting Expenses+Selling, General and Administrative) / Net Premiums Earned
    """


class LossRatio(MultiPeriodField):
    """
    A measure of operating performance for Insurance companies, as it shows the relationship between the premiums earned and the
    expenses related to claims. A number of 1 or lower is preferred, as this means the premiums exceed the expenses. Calculated as:
    Benefits, Claims and Loss Adjustment Expense, Net / Net Premiums Earned
    """


class DilutedEPSGrowth(MultiPeriodField):
    """
    The growth in the company's diluted earnings per share (EPS) on a percentage basis. Morningstar calculates the annualized growth
    percentage based on the underlying diluted EPS reported in the Income Statement within the company filings or reports.
    """


class DilutedContEPSGrowth(MultiPeriodField):
    """
    The growth in the company's diluted EPS from continuing operations on a percentage basis. Morningstar calculates the annualized
    growth percentage based on the underlying diluted EPS from continuing operations reported in the Income Statement within the
    company filings or reports.
    """


class DPSGrowth(MultiPeriodField):
    """
    The growth in the company's dividends per share (DPS) on a percentage basis. Morningstar calculates the annualized growth
    percentage based on the underlying DPS from its dividend database.  Morningstar collects its DPS from company filings and
    reports, as well as from third party sources.
    """


class EquityPerShareGrowth(MultiPeriodField):
    """
    The growth in the company's book value per share on a percentage basis. Morningstar calculates the annualized growth
    percentage based on the underlying equity and end of period shares outstanding reported in the company filings or reports.
    """


class RegressionGrowthofDividends5Years(MultiPeriodField):
    """
    The five-year growth rate of dividends per share, calculated using regression analysis.
    """


class FCFPerShareGrowth(MultiPeriodField):
    """
    The growth in the company's free cash flow per share on a percentage basis. Morningstar calculates the growth percentage based
    on the free cash flow divided by average diluted shares outstanding reported in the Financial Statements within the company filings
    or reports.
    """


class BookValuePerShareGrowth(MultiPeriodField):
    """
    The growth in the company's book value per share on a percentage basis. Morningstar calculates the growth percentage based on
    the common shareholder's equity reported in the Balance Sheet divided by the diluted shares outstanding within the company
    filings or reports.
    """


class NormalizedDilutedEPSGrowth(MultiPeriodField):
    """
    The growth in the company's Normalized Diluted EPS on a percentage basis.
    """


class NormalizedBasicEPSGrowth(MultiPeriodField):
    """
    The growth in the company's Normalized Basic EPS on a percentage basis.
    """


class SecurityReference:
    """
    Definition of the SecurityReference class
    """


class OperationRatios:
    """
    Definition of the OperationRatios class
    """


class CashFlowStatement:
    """
    Definition of the CashFlowStatement class
    """


class IncomeStatement:
    """
    Definition of the IncomeStatement class
    """


