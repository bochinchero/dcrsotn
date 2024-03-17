# Decred's State of the Network - {Issue.MonthStr} {Issue.Year}

Brief description goes here.

## Summary

Highlights go here.


## Network Metrics

### Transaction Count
_The Transaction Count reflects the daily number of transactions registered on the Decred network._

During the month of {Issue.MonthStr} the daily [transaction count](https://explorer.dcrdata.org/charts?chart=tx-count&zoom=ikd7pc00-lhgxp1c0&bin=day&axis=time&visibility=true-false) as reproted by dcrdata.org started at {txCount.Open} and closed at {txCount.Close}, reachiing a high of {txCount.High} on {txCount.High Date} and a low of {txCount.Low} on {txCount.Low Date}.

![Daily Transaction Count - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_TxCount.png?raw=true "Daily Transaction Count - Data: dcrdata.org")

The cumulative transaction count totaled {txCount.MoSum} over the month of {Issue.MonthStr}, representing a {txCount.MoSumChg} %increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Transaction Count - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_Tx_Count.png?raw=true "Monthly Transaction Count - Data: dcrdata.org")

### Transaction Volume
_Transaction Volume is a measure of the economic throughput by estimating the daily volume of coins that have been transfered using the Decred Network. [Coinmetrics' adjusted transaction volume](https://coinmetrics.io/introducing-adjusted-estimates/) removes obvious change and outputs spent within 4 blocks of their first expenditure to substract out the self-churn typical of exchanges, mixers, and stress test._

During the month of {Issue.MonthStr} the daily adjusted transaction volume in DCR as tracked by Coinmetrics started at {TxTfrValAdjNtv.Open} DCR and closed at {TxTfrValAdjNtv.Close} DCR, reachiing a high of {TxTfrValAdjNtv.High} DCR on {TxTfrValAdjNtv.High Date} and a low of {TxTfrValAdjNtv.Low} DCR on {TxTfrValAdjNtv.Low Date}.

![Daily Adjusted Transaction Volume (DCR) - Data: Coinmetrics](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_TxTfrValAdjNtv.png?raw=true "Daily Adjusted Transaction Volume (DCR) - Data: Coinmetrics")

The cumulative adjusted transaction volume totaled {TxTfrValAdjNtv.MoSum} DCR over the month of {Issue.MonthStr}, representing a {TxTfrValAdjNtv.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Adjusted Transaction Volume (DCR) - Data: Coinmetrics](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_TxTfrValAdjNtv.png?raw=true "Monthly Adjusted Transaction Volume (DCR) - Data: Coinmetrics")


In USD terms, during the month of {Issue.MonthStr} the daily [adjusted transaction volume](https://coinmetrics.io/introducing-adjusted-estimates/) in USD as tracked by Coinmetrics started at {TxTfrValAdjUSD.Open} USD and closed at {TxTfrValAdjUSD.Close} USD, reachiing a high of {TxTfrValAdjUSD.High} USD on {TxTfrValAdjUSD.High Date} and a low of {TxTfrValAdjUSD.Low} USD on {TxTfrValAdjUSD.Low Date}.

![Daily Adjusted Transaction Volume (USD) - Data: Coinmetrics](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_TxTfrValAdjUSD.png?raw=true "Daily Adjusted Transaction Volume (USD) - Data: Coinmetrics")

The cumulative adjusted transaction volume totaled {TxTfrValAdjUSD.MoSum} USD over the month of {Issue.MonthStr}, representing a {TxTfrValAdjUSD.MoSumChg} %increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Adjusted Transaction Volume (USD) - Data: Coinmetrics](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_TxTfrValAdjUSD.png?raw=true "Monthly Adjusted Transaction Volume (USD) - Data: Coinmetrics")


### Reachable Nodes
_Reachable Nodes are full nodes that can both send and receive connections from the Decred Network_

Throughout the month of {Issue.MonthStr} the daily reachable node count as tracked by [jholdstock's Decred Mapper](https://nodes.jholdstock.uk/) started at {NodeCount.Open} and closed at {NodeCount.Close}, reachiing a high of {NodeCount.High} on {txCount.High Date} and a low of {NodeCount.Low} on {NodeCount.Low Date}.

![Daily Node Distribution - Data: Decred Mapper](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Daily_NodeDistribution.png?raw=true "Daily Node Distribution - Data: Decred Mapper")

As of {Issue.NextMonth}1<sup>st</sup>, the distribution of dcrd versions across reachable nodes is:

![Reachable Node Distribution](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Reachable%20Node%20Versions.png?raw=true "Reachable Node Distribution")

###  Cumulative Block Size
_The cumulative Block Size is the total amount of data stored in blocks mined throughout the day in the Decred Network._

During the month of {Issue.MonthStr} the daily cumulative block size as tracked by [dcrdata.org](https://explorer.dcrdata.org/charts?chart=duration-btw-blocks&zoom=ikd7pc00-lhgxp1c0&bin=day&axis=time&visibility=true-false) started at {blkSize.Open} and closed at {blkSize.Close}, reachiing a high of {blkSize.High} on {blkSize.High Date} and a low of {blkSize.Low} on {blkSize.Low Date}.

![Daily Cumulative Block Size - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_BlockSize.png?raw=true "Daily Cumulative Block Size - Data: dcrdata.org")

Averaged over the month, the cumulative block size was {blkSize.MoMean} over the month of {Issue.MonthStr}, representing a {blkSize.MoMeanChg} %increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Cumulative Block Size - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_Blocksize.png?raw=true "Monthly Cumulative Block Size - Data: dcrdata.org")

###  Blockchain Size
_The Blockchain Size is the total amount of data stored since genesis in the Decred Network._

In the month of {Issue.MonthStr}, the size of the Decred blockchain grew {blkchainSize.High} over the month of {Issue.MonthStr}, representing a {blkchainSize.MoMaxChg} %increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Blockchain Size - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_BlockchainSize.png?raw=true "Monthly Blockchain Size - Data: dcrdata.org")

## Proof of Stake

### Staking Participation
_The Staking Participation is the percentage of DCR supply that is locked in tickets in the Decred Network._.

During the month of {Issue.MonthStr} the daily staking participation as tracked by dcrdata.org started at {stakepart.Open}% and closed at {stakepart.Close}%, reachiing a high of {stakepart.High}% on {stakepart.High Date} and a low of {stakepart.Low}% on {stakepart.Low Date}.

![Daily Staking Participation (%) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Participation_PC.png?raw=true "Daily Staking Participation (%) - Data: dcrdata.org")

The stake participation averaged {stakepart.MoMean}% over the month of {Issue.MonthStr}, representing a {stakepart.MoMeanChg}% increase/decrease over the average of the previous month of {Issue.PrevMonthStr}.


### Ticket Pool Value
_The Ticket Pool Value is the total number of DCR that is locked in tickets in the Decred network at any given time._.

During the month of {Issue.MonthStr} the daily value of the ticket pool as tracked by dcrdata.org started at {ticketpoolval.Open} DCR and closed at {ticketpoolval.Close} DCR, reachiing a high of {ticketpoolval.High} DCR on {ticketpoolval.High Date} and a low of {ticketpoolval.Low} DCR on {ticketpoolval.Low Date}.

![Daily Ticket Pool Value (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_TicketPoolVal_DCR.png?raw=true "Daily Ticket Pool Value (DCR) - Data: dcrdata.org")

The ticket pool value averaged {ticketpoolval.MoMean} DCR over the month of {Issue.MonthStr}, representing a {ticketpoolval.MoMeanChg}% increase/decrease over the average of the previous month of {Issue.PrevMonthStr}.


### Ticket Price
_The TIcket Price is the amount of DCR that must be locked in a ticket to partcipate in Decred's Proof-of-Stake system. Every 144 blocks (~12 hours), the stake difficulty algorithm calculates a new Ticket Price in an attempt to keep the Ticket Pool size near the target pool size of 40,960 tickets._

During the month of {Issue.MonthStr} the daily ticket price as tracked by dcrdata.org started at {ticketprice.Open} DCR and closed at {ticketprice.Close} DCR, reachiing a high of {stakepart.High} DCR on {ticketprice.High Date} and a low of {ticketprice.Low} DCR on {ticketprice.Low Date}.

![Daily Ticket Price (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_TicketPrice_DCR.png?raw=true "Daily Ticket Price (DCR) - Data: dcrdata.org")


The ticket price averaged {ticketprice.MoMean} DCR over the month of {Issue.MonthStr}, representing a {ticketprice.MoMeanChg}% increase/decrease over the average of the previous month of {Issue.PrevMonthStr}.

In USD terms, over the month of {Issue.MonthStr} the daily ticket price as tracked by dcrdata.org started at {ticketpriceUSD.Open} USD and closed at {ticketpriceUSD.Close} USD, reachiing a high of {ticketpriceUSD.High} USD on {ticketpriceUSD.High Date} and a low of {ticketpriceUSD.Low} DCR on {ticketpriceUSD.Low Date}.

![Daily Ticket Price (USD) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_TicketPrice_USD.png?raw=true "Daily Ticket Price (USD) - Data: dcrdata.org")



### Ticket Pool Size
_The Ticket Pool is the total number of live tickets in the Decred Network at any given time._.

During the month of {Issue.MonthStr} the daily ticket pool size as tracked by dcrdata.org started at {ticketpoolsize.Open}  and closed at {ticketpoolsize.Close}, reachiing a high of {ticketpoolsize.High} on {ticketpoolsize.High Date} and a low of {ticketpoolsize.Low} on {ticketprice.Low Date}.

IMAGE MISSING

The ticket pool size averaged {ticketpoolsize.MoMean} DCR over the month of {Issue.MonthStr}, representing a {ticketpoolsize.MoMeanChg}% increase/decrease over the average of the previous month of {Issue.PrevMonthStr}.


### Tickets Purchased
_Decred holders can time-lock DCR in exchange for tickets. Tickets grant their holder the ability to vote, and it is through ticket voting that major governance decisions are made._

During the month of {Issue.MonthStr} the daily number of missed votes started at {votesMissed.Open} and closed at {votesMissed.Close}, reachiing a high of {votesMissed.High} on {votesMissed.High Date} and a low of {votesMissed.Low} on {votesMissed.Low Date}.

![Daily Tickets Purchased](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Tickets_Purchased.png?raw=true "Daily Tickets Purchased")

The cumulative number of tickets purchased totaled {votesMissed.MoSum} over the month of {Issue.MonthStr}, representing a {votesMissed.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Tickets Purchased](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Ticket_Purchased.png?raw=true "Monthly Tickets Purchased")


### Tickets Voted
_In each block, 5 tickets are called to vote, determined by a lottery system. When a ticket is called, a nominated wallet must actively respond with a vote. ._

During the month of {Issue.MonthStr} the daily number of missed votes started at {votesMissed.Open} and closed at {votesMissed.Close}, reachiing a high of {votesMissed.High} on {votesMissed.High Date} and a low of {votesMissed.Low} on {votesMissed.Low Date}.

![Daily Tickets Purchased](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Tickets_Purchased.png?raw=true "Daily Tickets Purchased")

The cumulative number of tickets purchased totaled {votesMissed.MoSum} over the month of {Issue.MonthStr}, representing a {votesMissed.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Tickets Purchased](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Ticket_Purchased.png?raw=true "Monthly Tickets Purchased")


### Ticket Revocations
_Missed and expired tickets are revoked [automatically](https://github.com/decred/dcps/blob/master/dcp-0009/dcp-0009.mediawiki) to return the funds used to purchase the ticket to the stakeholder._

During the month of {Issue.MonthStr} the daily number of revocations started at {votesMissed.Open} and closed at {votesMissed.Close}, reachiing a high of {votesMissed.High} on {votesMissed.High Date} and a low of {votesMissed.Low} on {votesMissed.Low Date}.

![Daily Revoked Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Tickets_Revoked.png?raw=true "Daily Missed Votes")

The cumulative number of revoked tickets totaled {votesMissed.MoSum} over the month of {Issue.MonthStr}, representing a {votesMissed.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Revoked Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Tickets_Revoked.png?raw=true "Monthly Revoked Tickets")

Throughout the month of {Issue.MonthStr}, the breakdown of revocations between missed votes and and expired tickets is: 

![Monthly Ticket Revocation Distribution by Reason](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Monthly%20Ticket%20Revocation%20Distribution.png?raw=true "Monthly Ticket Revocation Distribution by Reason")

The distribution of ticket revocations across solo stakers and publicly reported Voting Service Providers (VSPs) is: 

![Monthly Ticket Revocation Distribution by Group](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Revoked%20Ticket%20Distribution.png?raw=true "Monthly Ticket Revocation Distribution by Group")

#### Missed Tickets
_Missed Tickets are tickets that do not have a wallet with voting rights online when called to vote. When a vote is marked as missed, no vote reward is created for that ticket._

During the month of {Issue.MonthStr} the daily number of missed tickets started at {votesMissed.Open} and closed at {votesMissed.Close}, reachiing a high of {votesMissed.High} on {votesMissed.High Date} and a low of {votesMissed.Low} on {votesMissed.Low Date}.

![Daily Missed Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Tickets_Missed.png?raw=true "Daily Missed Tickets")

The cumulative number of missed tickets totaled {votesMissed.MoSum} over the month of {Issue.MonthStr}, representing a {votesMissed.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Missed Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Tickets_Missed.png?raw=true "Monthly Missed Tickets")

The missed tickets ratio is calculated as the number of missed tickets out of all of the tickets called to vote for each respective group.

![Monthly Missed Ticket Ratio](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Missed_Ticket_Ratio.png?raw=true "Monthly Missed Tickets Ratio")

![Monthly Missed Ticket Ratio w/ VSPs](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Missed_Ticket_Ratio_Dist.png?raw=true "Monthly Missed Tickets Ratio w/ VSPs")

#### Expired Ticketss
_Expired tickets have reached the end of their window without being called to vote - these are then revoked, but do not grant a reward._

During the month of {Issue.MonthStr} the daily number of expired tickets started at {votesMissed.Open} and closed at {votesMissed.Close}, reachiing a high of {votesMissed.High} on {votesMissed.High Date} and a low of {votesMissed.Low} on {votesMissed.Low Date}.

![Daily Expired Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Tickets_Expired.png?raw=true "Daily Expired Tickets")

The cumulative number of expired tickets totaled {votesMissed.MoSum} over the month of {Issue.MonthStr}, representing a {votesMissed.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

![Monthly Expired Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Tickets_Expired.png?raw=true "Monthly Expired Tickets")

### Voting Service Providers
_Voting Service Providers (VSPs) offer a service whereby ticket buyers can delegate the act of voting to the VSP. The ticket-buyer instructs the VSP how their ticket should vote on any open rule change proposals, and shares voting rights with the VSP to take advantage of the voting infrastructure they provide (i.e. at least three always-online servers)._

_VSPs charge a fee for this service, which is paid upfront before the ticket is added to the VSPs voting wallets. This fee is generally 5% or less. VSPs do not take custody of DCR. By using them, you only delegate the voting rights of a ticket._

As of {Issue.NextMonth}1<sup>st</sup>, public Voting Service Providers are voting for a share of {vspShare.value} of the live tickets in the Ticket Pool.

![Live Ticket Distribution](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Live%20Ticket%20Distribution.png?raw=true "Live Ticket Distribution")

Among those public Voting Service Providers, the dsitribution of live tickets is:

![Live Ticket Distribution](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Voting%20Service%20Provider%20(VSP)%20-%20Live%20Ticket%20Distribution.png?raw=true "Live Ticket Distribution")


### Staker Revenue
_Staker Revenue is calculated as the amount of DCR earned by Proof-of-Stake voters from the block subsidy._

During the month of {Issue.MonthStr} the daily miner revenue started at {posRevenueDCR.Open} DCR and closed at {posRevenueDCR.Close} DCR, reachiing a high of {posRevenueDCR.High} DCR on {posRevenueDCR.High Date} and a low of {posRevenueDCR.Low} DCR on {posRevenueDCR.Low Date}.

IMAGE MISSING

The cumulative miner revenue totaled {posRevenueDCR.MoSum} DCR over the month of {Issue.MonthStr}, representing a {posRevenueDCR.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

IMAGE MISSING

In USD terms, over the month of {Issue.MonthStr}, the cumulative miner revenue totaled {posRevenueUSD.MoSum} USD, representing a {posRevenueUSD.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

IMAGE MISSING

## Proof of Work

### networkhashps
_networkhashps refers to the total combined computational power that is being used to mine and process transactions on a Proof-of-Work blockchain._

Throughout the month of {Issue.MonthStr} the daily networkhashps started at {networkhashps.Open} and closed at {networkhashps.Close}, reachiing a high of {networkhashps.High} on {networkhashps.High Date} and a low of {networkhashps.Low} on {networkhashps.Low Date}.

![Daily networkhashps](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_networkhashps.png?raw=true "Daily networkhashps")

As of {Issue.NextMonth}1<sup>st</sup>, the distribution of networkhashps across public pools, as reported by poolbay.io is:

![networkhashps Distribution](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/networkhashps%20Distribution.png?raw=true "networkhashps Distribution")


### Mean Duration Between Blocks
_Block time measures the time it takes the Proof-of-Work miners within the to verify transactions within one block and produce a new block. The mean duration calculates the average block time over a given day._


During the month of {Issue.MonthStr} the daily mean duration betweem blocks as tracked by [dcrdata.org](https://explorer.dcrdata.org/charts?chart=duration-btw-blocks&zoom=ikd7pc00-lhgxp1c0&bin=day&axis=time&visibility=true-false) started at {blkTime.Open} and closed at {blkTime.Close}, reachiing a high of {blkTime.High} on {blkTime.High Date} and a low of {blkTime.Low} on {blkTime.Low Date}.

![Daily Mean Block Duration - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_BlockTime.png?raw=true "Daily Mean Block Duration - Data: dcrdata.org")

Averaged over the month, the mean duration between blocks was {blkTime.MoMean} over the month of {Issue.MonthStr}, representing a {blkTime.MoMeanChg} %increase/decrease since the previous month of {Issue.PrevMonthStr}.

###  Fees
_Fees are paid to have your transaction included in a block. The default transaction fee for Decred is 0.0001 DCR/kB._

During the month of {Issue.MonthStr} the daily fees as tracked by [dcrdata.org](https://explorer.dcrdata.org/charts?chart=duration-btw-blocks&zoom=ikd7pc00-lhgxp1c0&bin=day&axis=time&visibility=true-false) started at {feesDCR.Open} DCR and closed at {feesDCR.Close} DCR, reachiing a high of {feesDCR.High} DCR on {feesDCR.High Date} and a low of {feesDCR.Low} DCR on {feesDCR.Low Date}.

IMAGE MISSING

The cumulative fees generated totaled {feesDCR.MoSum} DCR over the month of {Issue.MonthStr}, representing a {feesDCR.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

IMAGE MISSING

In USD terms, over the month of {Issue.MonthStr}, the cumulative fees generated totaled {feesUSD.MoSum} USD, representing a {feesUSD.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

IMAGE MISSING



### Miner Revenue
_Miner Revenue is calculated as the amount of DCR earned by Proof-of-Work miners from he block subsidy._

During the month of {Issue.MonthStr} the daily miner revenue started at {powRevenueDCR.Open} DCR and closed at {powRevenueDCR.Close} DCR, reachiing a high of {powRevenueDCR.High} DCR on {powRevenueDCR.High Date} and a low of {powRevenueDCR.Low} DCR on {powRevenueDCR.Low Date}.

IMAGE MISSING

The cumulative miner revenue totaled {powRevenueDCR.MoSum} DCR over the month of {Issue.MonthStr}, representing a {powRevenueDCR.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

IMAGE MISSING

In USD terms, over the month of {Issue.MonthStr}, the cumulative miner revenue totaled {powRevenueUSD.MoSum} USD, representing a {powRevenueUSD.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.

IMAGE MISSING


## Stakeshuffle 
_StakeShuffle is a non-custodial protocol that obfuscates ownership of DCR coins. Output addresses get anonymized via mixnet, a cryptographic protocol executed by mix-servers that provide anonymity for a group of senders._

### Mixing Volume
_Mixing volume is calculated as the cumulative amount of DCR that has been mixed through Stakeshuffle to anonymize outputs over a given time period._

During the month of {Issue.MonthStr} the daily Stakeshuffle mixing volume started at {PrivacyVol.Open} DCR and closed at {PrivacyVol.Close} DCR, reachiing a high of {PrivacyVol.High} DCR on {PrivacyVol.High Date} and a low of {PrivacyVol.Low} DCR on {PrivacyVol.Low Date}.

![StakeShuffle Daily Mixing Volume (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Daily_Volume_DCR.png?raw=true "StakeShuffle Daily Mixing Volume (DCR) - Data: dcrdata.org")

The cumulative mixing volume totaled {PrivacyVol.MoSum} DCR over the month of {Issue.MonthStr}, representing a {PrivacyVol.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.


![StakeShuffle Monthly Mixing Volume (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Monthly_Volume_DCR.png?raw=true "StakeShuffle Monthly Mixing Volume (DCR) - Data: dcrdata.org")

In USD terms, over the month of {Issue.MonthStr}, the cumulative mixing volume totaled {PrivacyVolUSD.MoSum} USD, representing a {PrivacyVolUSD.MoSumChg}% increase/decrease since the previous month of {Issue.PrevMonthStr}.


![StakeShuffle Monthly Mixing Volume (USD) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Monthly_Volume_USD.png?raw=true "StakeShuffle Monthly Mixing Volume (USD) - Data: dcrdata.org")

### Mixed and Unspent Supply
_Mixed and Unspent Supply is calculated as the cumulative amount of DCR in anonymized StakeShuffle outputs at a given point in time ._

During the month of {Issue.MonthStr} the daily Mixed and Unspent Supply started at {PrivacyMixedPC.Open} DCR and DCR at {PrivacyMixedPC.Close} DCR, reachiing a high of {PrivacyMixedPC.High} USD on {PrivacyMixedPC.High Date} and a low of {PrivacyMixedPC.Low} DCR on {PrivacyMixedPC.Low Date}.

![StakeShuffle Daily Mixed and Unspent Supply (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Daily_MixedUnspent_DCR.png?raw=true "StakeShuffle Daily Mixed and Unspent Supply (DCR) - Data: dcrdata.org")

In percentage terms over the total DCR circulating supply, throughout the month of {Issue.MonthStr} the mixed and unspent supply as tracked by dcrdata.org started at {PrivacyMixedDCR.Open} DCR and closed at {PrivacyMixedDCR.Close} DCR, reachiing a high of {PrivacyMixedDCR.High} DCR on {PrivacyMixedDCR.High Date} and a low of {PrivacyMixedDCR.Low} DCR on {PrivacyMixedDCR.Low Date}.

![StakeShuffle Daily Mixed and Unspent Supply (%) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Daily_MixedUnspent_PC.png?raw=true "StakeShuffle Daily Mixed and Unspent Supply (%) - Data: dcrdata.org")


## Decentralized Treasury

### Treasury Balance
_The treasury balance represents the sum of DCR across the decentralized treasury account and the legacy treasury._

As of {Issue.Month} 1<sup>st</sup>, the value of Decred's treasury balance was {treasuryBalanceDCR.Open}. Representing a 

## Lightning Network

_The Lightning Network is a decentralized system for instant, high-volume micropayments that removes the risk of delegating custody of funds to trusted third parties._

### Channel Count
_A Lightning channel is a bidirectional payment channel, meaning both parties can send and receive payments across the channel. Lightning channels comprise the Lightning Network and have a defined DCR capacity. This capacity is split between the two parties to the channel, and DCR is moved from one side of the channel to the other by Lightning transactions._

### Network Capacity
_Lightning capacity is the backbone and liquidity between nodes within the Decred Lightning network. Every new node joining the Decred lightning network must provide liquidity to spend._

During the month of {Issue.MonthStr} the daily network capacity of Decred's Lightning Network started at {PrivacyMixedPC.Open} DCR and closed at {PrivacyMixedPC.Close} DCR, reachiing a high of {PrivacyMixedPC.High} USD on {PrivacyMixedPC.High Date} and a low of {PrivacyMixedPC.Low} DCR on {PrivacyMixedPC.Low Date}.


### Node Count
_Lightning node is software that connects and interacts with the main Decred network and also within the Decred's Lightning Network itself_




## DCRDEX

_DCRDEX is a non-custodial, privacy-respecting exchange for trustless trading, powered by atomic swaps._

### Trading Volume
###  Liquidity

## Marlet Valuations

###  DCR Price

###  DCR Price (BTC)

###  Realized Value

###  NVT

###  RVT



###  RVT