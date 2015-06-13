class revenuesourcesdelta(collection):
    """ A collection revenue source delta objects. """
    pass

class revenuesourcedelta(object):
    pass
    
class revenuesources(collection):
    """ A collection of revenue sources. Revenue is broken down into units
    (sources) on the income statement. """
    def total(self):
        """ Just the total amount of revenue for the collection. """
        # TODO: Add total() aggregate function to collection.
        return self.total(lambda x: x.amount())

class revenuesource(object):
    """ Revenue sources are provided on on the income statement. """
    def __init__(self, revsrcs):
        self._revsrcs=revsrcs

    def percentage(self):
        """ The percent of revenue amoung all the other revenue sources in
        the revenuesources collection. """
        tot=self._revssrcs.total()
        amt=self.amount()
        return tot / amt * 100

    def name(self): 
        """ Name of the revenue source/unit. """
        pass

    def amount(self):
        """ Amount of the revenue source. """
        # Todo: Ensure a float is returned.
        pass

class reportingperiods(collection):
    pass

class reportingperiod(object):
    """ An annually or quarterly reporting period, which should have a
    reference to all the statements of the period. Computation and ratio
    accessors to compute values from the statements are located here. """

    TAX_RATE=.375
    def balancesheet(self): pass
    def cashflowstatement(self): pass
    def incomestatement(self): pass

    def inc(self): return self.incomestatement()
    def bs(self): return self.balancesheet()
    def cf(self): return self.cashflowstatement()
    def allstatements(self):
        return self.inc(), self.bs(), self.cf()

    def type(self): 
        """ Returns 'quaterly' or 'annually' depending on the type. """
        pass
    
    def freecashflow(self):
        """ Tells you the cash the company is generating during the normal
        course of doing business, including the cost of maintaining it's
        equipment. Can be confused with EBITDA. """
        return self.cashfromoperations() - self.capitalexpenditures()

    def yearssupplyofcash(self):
        """ Can be used to detect if a company to keep itself alive for the
        next few months. """
        return self.balancesheet().cashequivalents  
               / abs(self.freecashflow())

    def returnonequity(self):
        """ Net income divided by averagesshareholdersequity. 
        This is a key ratio. It tells you how much money is being generated
        by money entrusted to it by investors. An investment in assets may
        lower this ratio. This ratio should be compared to other companies
        in the same sector."""
        return inc.netincome() / self.averagesshareholdersequity(). 

    def averagesshareholdersequity(self):
        """ Calculated by taking the sharedholderequity from the current
        income statement, dividing it by the sharedholderequity from the
        last year's statement, and multiplying it by 2."""
        bs=self.bs()
        sheq=bs.sharedholderequity()
        prevsheq=bs.lastyears().sharedholderequity()
        return sheq/prevsheq * 2

    def returnoninvestedcapital(self):
        inc,bs=self.allstatements()
        ebit=inc.earningsbeforinterestsandtaxes()

        # Adjust ebit for taxes
        ebit *= (1-TAX_RATE)  # TODO: How to get tax rate for reporting period.

        # Calculate the total capital that the company possesses for the
        # current year.
        totcap = bs.equity() +
                 bs.currentportionoflongtermdebt() +
                 bs.longtermliabilities()

        # Calculate last years total cap
        lybs=bs.lastyears()
        lytotcap = lybs.equity() +
                   lybs.currentportionoflongtermdebt() +
                   lybs.longtermliabilities()

        # Calculate average total capital
        avgcap = (totcap + lytotcap) / 2.0

        # Calculate return on invested capital
        roic = ebit/avgcap

        # Return roic as percentage
        return roic * 100

class statements(collection):
    pass

class statement(object):
    pass

class proxystatement(statement):
    def __init__(self):
        self._bod = boardofdirectors()

class cashflowstatement(statement):
    
    ##########################################################################
    # Cash Flow from Operating Activities
    # (How much cash the company brings in or uses during normal course of 
    # business.)
    ##########################################################################
    def netincome(self):
        pass

    def deprecationamortization(self):
        """ Deprecation and amortization is the wear-and-tear on tangible
        and intangibles, respectivly. """
        pass

    def accountsreceivable(self):
        """ Money owed to the company by custorers on credit. """
        pass

    def accountspayable(self):
        """ Money owed to suppliers that have heretofore been payed with
        trade credit. """ 
        pass

    def inventories(self):
        """ The amount of inventory on hand. """
        pass

    def netcashprovidedbyoperations(self):
        """ The tally of all the above adjustments made to netincome. """
        pass
    
    ##########################################################################
    # Cash Flow from Investing Activities
    # (How much cash the company spent investing in itself. Captial
    # expenditures, acquisitions, proceeds from divestitures, etc.)
    ##########################################################################
    def netcashusedininvestingactivities(self):
        pass

    ##########################################################################
    # Cash Provided by Financial Activity
    # (After acconuting for all the cash brought in by borrowing and
    # isssuing stock, and cash used by extinguishing debt, buying back stock
    # and paying dividends, you get the final result)
    ##########################################################################

    def netcashprovidedbyorusedinfinancingactivity(self):
        """ The result of accounting for cash brought in by borrowing or
        issuing stock, cash used to extinguishing debt, buying back stocks
        and paying dividends. """
        pass




        

class balancesheet(statement):
    """ Reports on the financial health of a company. Indicates a company's
    ability to weather economic downturns. """
    def sharedholderequity(self):
        return self.assets() - self.liability()

    def equity(self):
        return self.sharedholderequity()

    ##########################################################################
    # Assets
    ##########################################################################

    def cash_commonsized(self): return self.cash() / self.totalassets() * 100
    def cash(self): 
        """ Cash on hand. """
        pass

    def cashequivalents_commonsized(self): return self.cashequivalents() / self.totalassets() * 100
    def cashequivalents(self):
        """ Cash the company has on hand that has is in short-term,
        high-quality investments. Cash and Cash Equivalents are often
        lumped together by analists. """
        pass

    def cashandcashequivalents(self):
        return self.cash() + self.cashequivalents()

    def marketablesecurities_commonsized(self): return self.marketablesecurities() / self.totalassets() * 100
    def marketablesecurities(self):
        """ Cash the company has invested in is not immediatly available
        because it is invested in high-quality debt that may take a quarter
        or two to mature. """
        pass

    def accountsreceivable_commonsized(self): return self.accountsreceivable() / self.totalassets() * 100
    def accountsreceivable(self):
        """ Money the company has in short-term IOU's such as debt-card
        transactions. """
        pass

    def inventories_commonsized(self): return self.inventories() / self.totalassets() * 100
    def inventories(self):
        """ Raw material the company has intended to make it's product. """
        pass

    def prepaidexpenses_commonsized(self): return self.prepaidexpenses() / self.totalassets() * 100
    def prepaidexpenses(self):
        """ Payments the company has made ahead of time to it's supplier.  """
        pass

    """ The following assets are considered long-term liabilities since the
    can't be turned into cash within at least a year. """

    def propertyplantandequipment_commonsized(self): return self.propertyplantandequipment() / self.totalassets() * 100
    def propertyplantandequipment(self)
        """ AKA PP&E. Building, computers, oil rigs, etc. """
        pass

    def goodwill_commonsized(self): return self.goodwill() / self.totalassets() * 100
    def goodwill(self):
        """ The amount paid for another company higher than the company is
        deemed to be worth according to accounting rules. """
        pass
    
    def otherintangibles_commonsized(self): return self.otherintangibles() / self.totalassets() * 100
    def otherintangibles(self):
        """ Patents, brands, trademarks, etc. """
        pass 

    def totalassets(self):
        return self.cash()                       + self.cashequivalents() +
                self.marketablesecurities()      + self.accountsreceivable() +
                self.inventories()               + self.prepaidexpenses() +
                self.propertyplantandequipment() + self.goods() +
                self.otherintangibles()


    ########################################################################
    # Liabilities
    ########################################################################

    def otherintangibles_commonsized(self): return self.otherintangibles() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def currentliabilites(self):
        """ Bills due within a year. """
        pass

    def accountspayable_commonsized(self): return self.accountspayable() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def accountspayable(self):
        """ Money owed to suppliers that have heretofore been payed with
        trade credit. """ 
        pass

    def shorttermdebt_commonsized(self): return self.shorttermdebt() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def shorttermdebt(self):
        """ Debt that the company must pay back within a year. """
        pass


    def currentportionoflongtermdebt_commonsized(self): return self.currentportionoflongtermdebt() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def currentportionoflongtermdebt(self):
        """The portion of long term debt that must be paied within a year."""
        pass

    def othercurrentliability_commonsized(self): return self.othercurrentliability() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def othercurrentliability(self):
        """ Miscellaneous liabilities. """
        pass

    """ The following are long-term liabilities, i.e., debts the company
    doesn't need to payoff within a year. """

    def longtermliabilities_commonsized(self): return self.longtermliabilities() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def longtermliabilities(self):
        """ Debt that doesn't need to be paid off in a year. """
        pass 
    
    def otherlongtermliabilities_commonsized(self): return self.otherlongtermliabilities() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def otherlongtermliabilities(self):
        """ Miscellaneous debt that doesn't need to be paid off in a year.
        """
        pass

    def deferredincometaxes_commonsized(self): return self.deferredincometaxes() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def deferredincometaxes(self):
        """ Taxes owed in the future. """
        pass

    def totalliability(self):
        return self.currentliabilites() + self.accountspayable() +
                self.shorttermdebt() + self.currentportionoflongtermdebt() +
                self.othercurrentliability() + self.longtermliabilities() +
                self.otherlongtermliabilities() +


    ##########################################################################
    # Stockholder Equity                                                     #
    ##########################################################################

    def preferredstock_commonsized(self): return self.preferredstock() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def preferredstock(self):
        pass

    def commonstock_commonsized(self): return self.commonstock() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def commonstock(self):
        pass

    def retainedearnings_commonsized(self): return self.retainedearnings() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def retainedearnings(self):
        """ Earnings that the company decides to keep as opposed to
        returning them to shareholders as dividends."""
        pass

    def treasurystocks_commonsized(self): return self.treasurystocks() / (self.totalliability() + self.totalshareholdersequity()) * 100
    def treasurystocks(self):
        """ The pool of unsued shares that the company owns itself. """
        pass

    def totalshareholdersequity(self):
        """ The value of the shareholders stake in the company. """
        pass

    
    ##########################################################################
    # Miscellaneous
    ##########################################################################
    def liability(self): 
        pass

    def sharesoutstanding(self):
        """ Total number of shares owned by the public as well as
        restricted share. """
        pass

    def restrictedshares(self):
        """ Shares held by officers and directors of the company. """
        pass

    def retainedearnings(self):
        """ The portion of profit the company keeps rather than giving to
        shareholders in the form of dividends."""
        pass

class incomestatementdelta(object):
    """ Shows the difference between the data in two different income
    statements. """

    def __init__(self, l, r):
        self._l, self._r = l,r

    def revenue(self):
        """ Shown the revenue growth between the two different
        statements."""
        return self.revenuesourcesdelta().total()

    def revenuesourcesdelta(self):
        """ The difference between the revenue units reported on the income
        statements l and r. """
        self._l.revenuesources() - self._r.revenuesources()

class expenses(collection):
    """ A collection of expenses reported on the income statement. """
    def __init__(self, stmt):
        self._incomestatement=stmt

        # Direct costs spent to create goods or services, e.g., cost of raw material. 
        self.add("costofgoodssold")
        self.add("marketing")
        self.add("r&d")
        self.add("administration")
        self.add("marketing")

        # Cost to restructure a company, paying severances, depreciation, etc.
        self.add("other")

        # Interest payed by the company to to debtors.
        self.add("interestexpense")
        self.add("taxes")

    def add(self, o):
        if isinstance(o, str):
            self.add(new expenses(o, self))
        elif isinstance(o, expense):
            collection.add(self, o)

    def costofgoodssold(self):
        return self['costofgoodssold']


    def operatingexpenses(self):
        """ A collection of indirect expenses incurred by conducting business
        which do not go into the direct product, e.g, marketing, R&D,
        administration.  aka: overhead. """
        r=expenses(stmt)
        for exp in self:
            if exp.name() in ('marketing', 'r&d', 'administration'):
                r.add(exp)
        return r

    def incomestatement(self):
        """ The incomestatement object where this expense is reported. """
        return self._incomestatement

    def amount(self)
        return self.total(lambda e: e.amount())

class expense(object):
    """ An expense reported on the income statement. """

    def __init__(self, name, expenses):
        self._name=name
        self._expenses=expenses

    def incomestatement(self):
        """ The incomestatement object where this expense is reported. """
        self._expenses.incomestatement()

    def cost(self):
        """ The dollor amount of the expense. """
        pass

    def name(self):
        """ An identifier for the expense such as "costofgoodssold",
        "marketvalue", etc. """
        pass

    def commonsized(self):
        """ The percentage of the expense compared to the income statements
        total revenue. """
        rev=self.incomestatement().revenue()
        cost=self.cost()
        return rev/cost*100
    
class incomestatement(statement):
    def __init__(self):
        self._expenses=None

    def __lt__(self, stmt):
        """ Returns an incomestatementdelta object to represent the
        difference between self and stmt. """
        return incomestatementdelta(self, stmt)

    def netincome(self):
        """ AKA profit. revenue - costs.  Comparing netincome with revenue
        over the years can quickly show how well costs are controlled as
        demand grows. """
        rev = self.revenue()
        exps = self.expenses().amount()
        return rev - expenses 

    def basicearningspershare(self):    
        """ The amout of netprofit a share owner is entitled to."""

        # TODO: The dividends of prefered stock should be subtracted from
        # the return value.
        return self.netincome() / self.company().sharesoutstanding()

    def dilutedearningspershare(self):    
        """ A measure of how much a company earned based on each share of
        stock. Diluted EPS is usually the EPS reported in the media as it
        is more conservative than basicearningspershare. """

        return self.netincome() / self.company().possiblesharesoutstanding()

    def expenses(self):
        if self._expenses==None:
            self._expenses=expenses(self)
        return self._expenses

    def sales(self): return self.revenue()
        
    def revenue(self):
        """ The amount of money brought in by a company from selling goods
        and services. """
        return self.revenuesources.total()

    def grossprofit(self):
        """ A simple way to look a profitability. revenue - costofgoodssold.  
        The amount a company makes after subtracting costs directly
        connected with production. See grossprofitmargin.
        """
        return self.revenue() - self.expenses().costofgoodssold().amount()

    def grossprofitmargin(self):
        """ Tells you how much of the revenue is kept, after paying direct
        costs, relative to sales. The average gross margin on the S&P 500
        is 45.1 percent. This is no a useful metric for software and
        internet companies since their majority of costs are overhead.  """
        return self.grossprofit() / self.revenue() * 100

    def operatingprofit(self):
        """ Revenue minue operating expenses. See operatingprofitmargin. """
        opexps = self.expenses().operatingexpenses().amount()
        return self.revenue() - opexps

    def operatingprofitmargin(self):
        """ How much the company keeps of the revenue after paying direct
        costs and overhead. The average S&P 500 company's operating profit
        margin is 18%. """
        return self.operatingprofit() / self.revenue() * 100
    
    def revenuesources(self):
        """ The collection of revenue sources for the income statement. """
        pass

    def sga(self): return sellinggeneraladministrativeexpenses()

    def sellinggeneraladministrativeexpenses(self)
        pass
    
    def otherincome(self):
        """ Money from other sources such as winning a legal settlement on
        selling a factory. """.
        pass

    def costofsales(self): return self.costofgoodssold()

    def costofgoodssold(self):
        return self.expenses()['costofgoodssold']

    def earningsbeforinterestsandtaxes(self):
        exps=self.expenses()
        cogs=exps['costofgoodssold']
        opexps=exps['operatingexpenses']
        other=exps['other']
        rev = self.revenue()

        return rev - cogs - opexps - other
class businessrelationships(collection) pass

class businessrelationship(object):
    def __init__(self, person, company, relationshiptype):
        pass

class persons(collection): pass

class person(object): pass

class auditor(object):
    """ The company hired by the company which checks the book and
    records to make sure it's representing everything accurately. Data
    about the auditor will appear on the proxy statement. """
    def fees(self):
        """ Fees recieved by the auditor for reviewing the books. """
        pass
    def auditrelatedfees(self):
        """ Fees directly related to the audit process. """
        pass

    def taxfees(self):
        """ Fees for the company's use of the auditor for tax help. """
        pass

    def otherfees(self):
        """ Consulting fees for information services and other advisory
        services that have nothing to do with the company's audit."""



class boardmember(person):
    def compensation(self):
        """ Compensation received for being a board member. Shouldn't be
        too high or too low. We also need a delta object for boardmembers
        because the difference between compensation from period to period
        is significant. Compensation between companies of similar size is
        also significant. """
        pass 

    def workexperience(self):
        """ The work experience that this person has (obviously). I'm not
        really sure how to formalize this at the moment. """
        pass

    def education(self):
        """ This should probably be a collection of degrees and
        certificates. """
        pass

    def boardsmemberships(self):
        """ Returns a boards collection object that the person currently
        sits on. If a board director sits on many other boards, it might
        indicate they don't have much time to spend attending to overseeing
        any given company. """
        pass

    def businessrelationships(self):
        """ Returns a businessrelationships collection object detailing the
        connections the person has to companies. """
        pass



class boards(collection): pass


class board(object){
    def __init__(self):
        self._members = persons()

    def numberOfMeetings(self):
        """ The number of meetings the board had during a certain period.
        This number will usually be set by the proxystatement object. """
        

class auditcommittee(board):
    """ The audit committee is directly responsible for connecting with the
    accounthing firm that checks over the company's books and records. """
    pass

class compensationcommittee(board):
    """ Members determine how much to pay the people running the company. """
    pass

class nominatingcommittee(board):
    """ Evaluates candidates for key jobs at the company. """
    pass

class boardofdirectors(board):
    """ Acts as a watch dog for investors and ensures the company's money
    is managed properly. """
    pass







class company(object):
    def __init__(self):
        self._statements=None

    def statements(self):
        if self._statements==None:
            self._statements==statements()
        return self._statements

    def marketvalue(self):
        return self.shareprice() * self.sharesoutstanding()

    def shareprace(self):
        pass
    
    def sharesoutstanding(self):
        # note: .last() should be a member of 
        # the collection abstract object.
        return self.statements().balancesheets().last()

    def possiblesharesoutstanding(self):
        # This includes all the shares that could come into existence as a
        # result of employees converting options to shares. Diluted EPS is 
        # based on this.
        pass
