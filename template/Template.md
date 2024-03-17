# Decred's State of the Network - {Issue.MonthStr} {Issue.Year}

Brief description goes here.



## Summary

Highlights go here.

## Contents

* [Network Metrics](#Network-Metrics)
  * [Transaction Count](#transaction-count)
  * [Transaction Volume](#transaction-volume)
  * [Reachable Nodes](#reachable-nodes)
  * [Cumulative Block Size](#cumulative-block-size)
  * [Blockchain Size](#blockchain-size)
  * [New Issuance](#new-issuance)
* [Proof of Stake](#proof-of-stake)
  * [Staking Participation](#staking-participation)
  * [Ticket Pool Value](#ticket-pool-value)
  * [Ticket Price](#ticket-price)
  * [Ticket Pool Size](#ticket-pool-size)
  * [Tickets Purchased](#tickets-purchased)
  * [Tickets Voted](#tickets-voted)
  * [Ticket Revocations](#ticket-revocations)
  * [Missed Tickets](#missed-tickets)
  * [Expired Tickets](#expired-ticketss)
  * [Voting Service Providers](#voting-service-providers)
* [Proof of Work](#proof-of-work)
  * [Hashrate](#hashrate)
  * [Mean Duration Beetween Blocks](#mean-duration-between-blocks)
  * [fees](#fees)
* [Stakeshuffle](#stakeshuffle)
  * [Mixing Volume](#mixing-volume)
  * [Mixed and Unspent Supply](#mixed-and-unspent-supply)
* [Decentralized Treasury](#decentralized-treasury)
  * [Treasury Balance](#treasury-balance)
  * [Treasury Flows](#treasury-flows)
* [Lightning Network](#decentralized-treasury)
  * [Channel Count](#channel-count)
  * [Network Capacity](#network-capacity)
  * [Node Count](#node-count)
* [Decentralized Exchange](#decentralized-exchange)
  * [Trading Volume](#trading-volume)
* [Markets & Valuations](#markets--valuations)
  * [DCR/USD](#dcrusd)
  * [DCR/BTC](#dcrbtc)

## Network Metrics

### Transaction Count
_The Transaction Count reflects the daily number of transactions registered on the Decred network._

During the month of {Issue.MonthStr}, the daily [transaction count](https://explorer.dcrdata.org/charts?chart=tx-count&zoom=ikd7pc00-lhgxp1c0&bin=day&axis=time&visibility=true-false) as reproted by dcrdata.org opened at {txCount.Open} and closed at {txCount.Close}, reaching a high of {txCount.High} on {txCount.High Date} and a low of {txCount.Low} on {txCount.Low Date}.

![Daily Transaction Count - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_TxCount.png?raw=true "Daily Transaction Count - Data: dcrdata.org")

The cumulative transaction count totaled {txCount.MoSum} over the month of {Issue.MonthStr}, representing a {txCount.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Transaction Count - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_Tx_Count.png?raw=true "Monthly Transaction Count - Data: dcrdata.org")

[Back to Contents](#contents)

### Transaction Volume
_Transaction Volume is a measure of the economic throughput by estimating the daily volume of coins that have been transfered using the Decred Network. [Coinmetrics' adjusted transaction volume](https://coinmetrics.io/introducing-adjusted-estimates/) removes obvious change and outputs spent within 4 blocks of their first expenditure to substract out the self-churn typical of exchanges, mixers, and stress test._

During the month of {Issue.MonthStr}, the daily adjusted transaction volume in DCR as tracked by Coinmetrics opened at {TxTfrValAdjNtv.Open} DCR and closed at {TxTfrValAdjNtv.Close} DCR, reaching a high of {TxTfrValAdjNtv.High} DCR on {TxTfrValAdjNtv.High Date} and a low of {TxTfrValAdjNtv.Low} DCR on {TxTfrValAdjNtv.Low Date}.

![Daily Adjusted Transaction Volume (DCR) - Data: Coinmetrics](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_TxTfrValAdjNtv.png?raw=true "Daily Adjusted Transaction Volume (DCR) - Data: Coinmetrics")

The cumulative adjusted transaction volume totaled {TxTfrValAdjNtv.MoSum} DCR over the month of {Issue.MonthStr}, representing a {TxTfrValAdjNtv.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Adjusted Transaction Volume (DCR) - Data: Coinmetrics](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_TxTfrValAdjNtv.png?raw=true "Monthly Adjusted Transaction Volume (DCR) - Data: Coinmetrics")


In USD terms, During the month of {Issue.MonthStr}, the daily [adjusted transaction volume](https://coinmetrics.io/introducing-adjusted-estimates/) in USD as tracked by Coinmetrics opened at {TxTfrValAdjUSD.Open} USD and closed at {TxTfrValAdjUSD.Close} USD, reaching a high of {TxTfrValAdjUSD.High} USD on {TxTfrValAdjUSD.High Date} and a low of {TxTfrValAdjUSD.Low} USD on {TxTfrValAdjUSD.Low Date}.

![Daily Adjusted Transaction Volume (USD) - Data: Coinmetrics](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_TxTfrValAdjUSD.png?raw=true "Daily Adjusted Transaction Volume (USD) - Data: Coinmetrics")

The cumulative adjusted transaction volume totaled {TxTfrValAdjUSD.MoSum} USD over the month of {Issue.MonthStr}, representing a {TxTfrValAdjUSD.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Adjusted Transaction Volume (USD) - Data: Coinmetrics](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_TxTfrValAdjUSD.png?raw=true "Monthly Adjusted Transaction Volume (USD) - Data: Coinmetrics")

[Back to Contents](#contents)

### Reachable Nodes
_Reachable Nodes are full nodes that can both send and receive connections from the Decred Network_

Throughout the month of {Issue.MonthStr}, the daily reachable node count as tracked by [jholdstock's Decred Mapper](https://nodes.jholdstock.uk/) opened at {NodeCount.Open} and closed at {NodeCount.Close}, reaching a high of {NodeCount.High} on {txCount.High Date} and a low of {NodeCount.Low} on {NodeCount.Low Date}.

![Daily Node Distribution - Data: Decred Mapper](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Daily_NodeDistribution.png?raw=true "Daily Node Distribution - Data: Decred Mapper")

As of {Issue.nextMonthStr} 1<sup>st</sup>, the distribution of dcrd versions across reachable nodes is:

![Reachable Node Distribution](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Reachable%20Node%20Versions.png?raw=true "Reachable Node Distribution")

[Back to Contents](#contents)

###  Cumulative Block Size
_The cumulative Block Size is the total amount of data stored in blocks mined throughout the day in the Decred Network._

During the month of {Issue.MonthStr}, the daily cumulative block size as tracked by [dcrdata.org](https://explorer.dcrdata.org/charts?chart=duration-btw-blocks&zoom=ikd7pc00-lhgxp1c0&bin=day&axis=time&visibility=true-false) opened at {blkSize.Open} and closed at {blkSize.Close}, reaching a high of {blkSize.High} on {blkSize.High Date} and a low of {blkSize.Low} on {blkSize.Low Date}.

![Daily Cumulative Block Size - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_BlockSize.png?raw=true "Daily Cumulative Block Size - Data: dcrdata.org")

Averaged over the month, the cumulative block size was {blkSize.MoMean} over the month of {Issue.MonthStr}, representing a {blkSize.MoMeanChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Cumulative Block Size - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_Blocksize.png?raw=true "Monthly Cumulative Block Size - Data: dcrdata.org")

[Back to Contents](#contents)

###  Blockchain Size
_The Blockchain Size is the total amount of data stored since genesis in the Decred Network._

In the month of {Issue.MonthStr}, the size of the Decred blockchain grew {blkchainSize.High}, representing a {blkchainSize.MoMaxChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Blockchain Size - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_BlockchainSize.png?raw=true "Monthly Blockchain Size - Data: dcrdata.org")

[Back to Contents](#contents)

### New Issuance
_New blocks are discovered by the proof-of-work miners roughly every 5 minutes, and each time this occurs new decred are created. As of block 794,368, the block reward is split as follows:_
* _1% goes to the PoW miner who found the block_
* _89% goes to the PoS voters on that block (17.8% to each of the 5 voters)_
* _10% goes towards the Decred Treasury_

In the month of {Issue.MonthStr}, {issuanceDCR.MoSum} DCR were generated via block rewards, representing an average inflation of {inflationRate.MoMean}%. 

![Monthly New Issuance (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/New_Issuance_DCR.png?raw=true "Monthly New Issuance (DCR)")

Of the block rewards generated, {issuancePoW.MoSum} DCR was received by Proof-of-Work miners, {issuancePoS.MoSum} DCR was received by Proof-of-Stake voters and {issuanceTres.MoSum} DCR was added to the Treasury.

![Distribution of New Issuance (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/New%20Issuance%20Distribution%20(DCR).png?raw=true "New Issuance Distribution (DCR)")

In USD terms, {issuancePoWUSD.MoSum} USD was received by Proof-of-Work miners, {issuanceUSD.MoSum} USD was received by Proof-of-Stake voters and {issuanceTresUSD.MoSum} USD was added to the Treasury.

![Monthly New Issuance (USD) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/New_Issuance_USD.png?raw=true "Monthly New Issuance (USD)")

[Back to Contents](#contents)

## Proof of Stake

### Staking Participation
_The Staking Participation is the percentage of DCR supply that is locked in tickets in the Decred Network._

During the month of {Issue.MonthStr}, the daily staking participation as tracked by dcrdata.org opened at {stakepart.Open}% and closed at {stakepart.Close}%, reaching a high of {stakepart.High}% on {stakepart.High Date} and a low of {stakepart.Low}% on {stakepart.Low Date}.

![Daily Staking Participation (%) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Participation_PC.png?raw=true "Daily Staking Participation (%) - Data: dcrdata.org")

The stake participation averaged {stakepart.MoMean}% over the month of {Issue.MonthStr}, representing a {stakepart.MoMeanChg}% change over the average of the previous month of {Issue.PrevMonthStr}.

[Back to Contents](#contents)

### Ticket Pool Value
_The Ticket Pool Value is the total number of DCR that is locked in tickets in the Decred network at any given time._

During the month of {Issue.MonthStr}, the daily value of the ticket pool as tracked by dcrdata.org opened at {ticketpoolval.Open} DCR and closed at {ticketpoolval.Close} DCR, reaching a high of {ticketpoolval.High} DCR on {ticketpoolval.High Date} and a low of {ticketpoolval.Low} DCR on {ticketpoolval.Low Date}.

![Daily Ticket Pool Value (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_TicketPoolVal_DCR.png?raw=true "Daily Ticket Pool Value (DCR) - Data: dcrdata.org")

The ticket pool value averaged {ticketpoolval.MoMean} DCR over the month of {Issue.MonthStr}, representing a {ticketpoolval.MoMeanChg}% change over the average of the previous month of {Issue.PrevMonthStr}.

[Back to Contents](#contents)

### Ticket Price
_The TIcket Price is the amount of DCR that must be locked in a ticket to partcipate in Decred's Proof-of-Stake system. Every 144 blocks (~12 hours), the stake difficulty algorithm calculates a new Ticket Price in an attempt to keep the Ticket Pool size near the target pool size of 40,960 tickets._

During the month of {Issue.MonthStr}, the daily ticket price as tracked by dcrdata.org opened at {ticketprice.Open} DCR and closed at {ticketprice.Close} DCR, reaching a high of {stakepart.High} DCR on {ticketprice.High Date} and a low of {ticketprice.Low} DCR on {ticketprice.Low Date}.

![Daily Ticket Price (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_TicketPrice_DCR.png?raw=true "Daily Ticket Price (DCR) - Data: dcrdata.org")

The ticket price averaged {ticketprice.MoMean} DCR over the month of {Issue.MonthStr}, representing a {ticketprice.MoMeanChg}% change over the average of the previous month of {Issue.PrevMonthStr}.

In USD terms, over the month of {Issue.MonthStr}, the daily ticket price as tracked by dcrdata.org opened at {ticketpriceUSD.Open} USD and closed at {ticketpriceUSD.Close} USD, reaching a high of {ticketpriceUSD.High} USD on {ticketpriceUSD.High Date} and a low of {ticketpriceUSD.Low} DCR on {ticketpriceUSD.Low Date}.

![Daily Ticket Price (USD) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_TicketPrice_USD.png?raw=true "Daily Ticket Price (USD) - Data: dcrdata.org")


[Back to Contents](#contents)

### Ticket Pool Size
_The Ticket Pool is the total number of live tickets in the Decred Network at any given time._

During the month of {Issue.MonthStr}, the daily ticket pool size as tracked by dcrdata.org opened at {ticketpoolsize.Open}  and closed at {ticketpoolsize.Close}, reaching a high of {ticketpoolsize.High} on {ticketpoolsize.High Date} and a low of {ticketpoolsize.Low} on {ticketprice.Low Date}.

![Daily Ticket Pool Size - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_TicketPoolSize.png?raw=true "Daily Ticket Pool Size - Data: dcrdata.org")

The ticket pool size averaged {ticketpoolsize.MoMean} DCR over the month of {Issue.MonthStr}, representing a {ticketpoolsize.MoMeanChg}% change over the average of the previous month of {Issue.PrevMonthStr}.

[Back to Contents](#contents)

### Tickets Purchased
_Decred holders can time-lock DCR in exchange for tickets. Tickets grant their holder the ability to vote, and it is through ticket voting that major governance decisions are made._

During the month of {Issue.MonthStr}, the daily number of missed votes opened at {tickets.Open} and closed at {tickets.Close}, reaching a high of {tickets.High} on {tickets.High Date} and a low of {tickets.Low} on {tickets.Low Date}.

![Daily Tickets Purchased](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Tickets_Purchased.png?raw=true "Daily Tickets Purchased")

The cumulative number of tickets purchased totaled {tickets.MoSum} over the month of {Issue.MonthStr}, representing a {tickets.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Tickets Purchased](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Ticket_Purchased.png?raw=true "Monthly Tickets Purchased")

[Back to Contents](#contents)

### Tickets Voted
_In each block, 5 tickets are called to vote, determined by a lottery system. When a ticket is called, a nominated wallet must actively respond with a vote._

During the month of {Issue.MonthStr}, the daily number of votes opened at {votes.Open} and closed at {votes.Close}, reaching a high of {votes.High} on {votes.High Date} and a low of {votes.Low} on {votes.Low Date}.

![Daily Votes](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Votes.png?raw=true "Daily Votes")

The cumulative number of votes totaled {votes.MoSum} over the month of {Issue.MonthStr}, representing a {votes.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Votes](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Votes.png?raw=true "Monthly Votes")

[Back to Contents](#contents)

### Ticket Revocations
_Missed and expired tickets are revoked [automatically](https://github.com/decred/dcps/blob/master/dcp-0009/dcp-0009.mediawiki) to return the funds used to purchase the ticket to the stakeholder._

During the month of {Issue.MonthStr}, the daily number of revocations opened at {ticketsRevoked.Open} and closed at {ticketsRevoked.Close}, reaching a high of {ticketsRevoked.High} on {ticketsRevoked.High Date} and a low of {ticketsRevoked.Low} on {ticketsRevoked.Low Date}.

![Daily Revoked Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Tickets_Revoked.png?raw=true "Daily Missed Votes")

The cumulative number of revoked tickets totaled {ticketsRevoked.MoSum} over the month of {Issue.MonthStr}, representing a {ticketsRevoked.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Revoked Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Tickets_Revoked.png?raw=true "Monthly Revoked Tickets")

Throughout the month of {Issue.MonthStr}, the breakdown of revocations between missed votes and expired tickets is as follows: 

![Monthly Ticket Revocation Distribution by Reason](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Monthly%20Ticket%20Revocation%20Distribution.png?raw=true "Monthly Ticket Revocation Distribution by Reason")

The distribution of ticket revocations across solo stakers and publicly reported Voting Service Providers (VSPs) is as follows: 

![Monthly Ticket Revocation Distribution by Group](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Revoked%20Ticket%20Distribution.png?raw=true "Monthly Ticket Revocation Distribution by Group")

[Back to Contents](#contents)

#### Missed Tickets
_Missed Tickets are tickets that do not have a wallet with voting rights online when called to vote. When a vote is marked as missed, no vote reward is created for that ticket._

During the month of {Issue.MonthStr}, the daily number of missed tickets opened at {votesMissed.Open} and closed at {votesMissed.Close}, reaching a high of {votesMissed.High} on {votesMissed.High Date} and a low of {votesMissed.Low} on {votesMissed.Low Date}.

![Daily Missed Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Tickets_Missed.png?raw=true "Daily Missed Tickets")

The cumulative number of missed tickets totaled {votesMissed.MoSum} over the month of {Issue.MonthStr}, representing a {votesMissed.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Missed Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Tickets_Missed.png?raw=true "Monthly Missed Tickets")

The missed tickets ratio is calculated as the number of missed tickets out of all of the tickets called to vote for each respective group.

![Monthly Missed Ticket Ratio](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Missed_Ticket_Ratio.png?raw=true "Monthly Missed Tickets Ratio")

![Monthly Missed Ticket Ratio w/ VSPs](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Missed_Ticket_Ratio_Dist.png?raw=true "Monthly Missed Tickets Ratio w/ VSPs")

[Back to Contents](#contents)

#### Expired Ticketss
_Expired tickets have reached the end of their window without being called to vote - these are then revoked, but do not grant a reward._

During the month of {Issue.MonthStr}, the daily number of expired tickets opened at {ticketExpired.Open} and closed at {ticketExpired.Close}, reaching a high of {ticketExpired.High} on {ticketExpired.High Date} and a low of {ticketExpired.Low} on {ticketExpired.Low Date}.

![Daily Expired Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Daily_Tickets_Expired.png?raw=true "Daily Expired Tickets")

The cumulative number of expired tickets totaled {ticketExpired.MoSum} over the month of {Issue.MonthStr}, representing a {ticketExpired.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Expired Tickets - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Staking_Monthly_Tickets_Expired.png?raw=true "Monthly Expired Tickets")

[Back to Contents](#contents)

### Voting Service Providers
_Voting Service Providers (VSPs) offer a service whereby ticket buyers can delegate the act of voting to the VSP. The ticket-buyer instructs the VSP how their ticket should vote on any open rule change proposals, and shares voting rights with the VSP to take advantage of the voting infrastructure they provide (i.e. at least three always-online servers)._

_VSPs charge a fee for this service, which is paid upfront before the ticket is added to the VSPs voting wallets. This fee is generally 5% or less. VSPs do not take custody of DCR. By using them, you only delegate the voting rights of a ticket._

As of {Issue.nextMonthStr} 1<sup>st</sup>, public Voting Service Providers are voting for a share of {vspShare.value} of the live tickets in the Ticket Pool.

![Live Ticket Distribution](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Live%20Ticket%20Distribution.png?raw=true "Live Ticket Distribution")

Among those public Voting Service Providers, the dsitribution of live tickets is:

![Live Ticket Distribution](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Voting%20Service%20Provider%20(VSP)%20-%20Live%20Ticket%20Distribution.png?raw=true "Live Ticket Distribution")

[Back to Contents](#contents)

## Proof of Work

### Hashrate
_Hashrate refers to the total combined computational power that is being used to mine and process transactions on a Proof-of-Work blockchain._

Throughout the month of {Issue.MonthStr}, the daily hashrate opened at {networkhashps.Open} and closed at {networkhashps.Close}, reaching a high of {networkhashps.High} on {networkhashps.High Date} and a low of {networkhashps.Low} on {networkhashps.Low Date}.

![Daily networkhashps](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_networkhashps.png?raw=true "Daily networkhashps")

As of {Issue.nextMonthStr} 1<sup>st</sup>, the distribution of hashrate across public pools, as reported by poolbay.io is:

![hashrate Distribution](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/hashrate%20Distribution.png?raw=true "hashrate Distribution")

[Back to Contents](#contents)

### Mean Duration Between Blocks
_Block time measures the time it takes the Proof-of-Work miners within the to verify transactions within one block and produce a new block. The mean duration calculates the average block time over a given day._

During the month of {Issue.MonthStr}, the daily mean duration between blocks as tracked by [dcrdata.org](https://explorer.dcrdata.org/charts?chart=duration-btw-blocks&zoom=ikd7pc00-lhgxp1c0&bin=day&axis=time&visibility=true-false) opened at {blkTime.Open} and closed at {blkTime.Close}, reaching a high of {blkTime.High} on {blkTime.High Date} and a low of {blkTime.Low} on {blkTime.Low Date}.

![Daily Mean Block Duration - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Daily_BlockTime.png?raw=true "Daily Mean Block Duration - Data: dcrdata.org")

Averaged over the month, the mean duration between blocks was {blkTime.MoMean} over the month of {Issue.MonthStr}, representing a {blkTime.MoMeanChg}% change over the previous month of {Issue.PrevMonthStr}.

[Back to Contents](#contents)

###  Fees
_Fees are paid to have your transaction included in a block. The default transaction fee for Decred is 0.0001 DCR/kB._

During the month of {Issue.MonthStr}, the cumulative fees, as tracked by [dcrdata.org](https://explorer.dcrdata.org/charts?chart=duration-btw-blocks&zoom=ikd7pc00-lhgxp1c0&bin=day&axis=time&visibility=true-false), totaled {feesDCR.MoSum} DCR, representing a {feesDCR.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![Monthly Fees (DCR)- Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Network_Monthly_Fees_DCR.png?raw=true "Monthly Fees (DCR) - Data: dcrdata.org")

[Back to Contents](#contents)

## Stakeshuffle 
_StakeShuffle is a non-custodial protocol that obfuscates ownership of DCR coins. Output addresses get anonymized via mixnet, a cryptographic protocol executed by mix-servers that provide anonymity for a group of senders._

### Mixing Volume
_Mixing volume is calculated as the cumulative amount of DCR that has been mixed through Stakeshuffle to anonymize outputs over a given time period._

During the month of {Issue.MonthStr}, the daily Stakeshuffle mixing volume opened at {PrivacyVol.Open} DCR and closed at {PrivacyVol.Close} DCR, reaching a high of {PrivacyVol.High} DCR on {PrivacyVol.High Date} and a low of {PrivacyVol.Low} DCR on {PrivacyVol.Low Date}.

![StakeShuffle Daily Mixing Volume (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Daily_Volume_DCR.png?raw=true "StakeShuffle Daily Mixing Volume (DCR) - Data: dcrdata.org")

The cumulative mixing volume totaled {PrivacyVol.MoSum} DCR over the month of {Issue.MonthStr}, representing a {PrivacyVol.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![StakeShuffle Monthly Mixing Volume (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Monthly_Volume_DCR.png?raw=true "StakeShuffle Monthly Mixing Volume (DCR) - Data: dcrdata.org")

In USD terms, over the month of {Issue.MonthStr}, the cumulative mixing volume totaled {PrivacyVolUSD.MoSum} USD, representing a {PrivacyVolUSD.MoSumChg}% change over the previous month of {Issue.PrevMonthStr}.

![StakeShuffle Monthly Mixing Volume (USD) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Monthly_Volume_USD.png?raw=true "StakeShuffle Monthly Mixing Volume (USD) - Data: dcrdata.org")

[Back to Contents](#contents)

### Mixed and Unspent Supply
_Mixed and Unspent Supply is calculated as the cumulative amount of DCR in anonymized StakeShuffle outputs at a given point in time._

During the month of {Issue.MonthStr}, the daily Mixed and Unspent Supply opened at {PrivacyMixedPC.Open} DCR and DCR at {PrivacyMixedPC.Close} DCR, reaching a high of {PrivacyMixedPC.High} DCR on {PrivacyMixedPC.High Date} and a low of {PrivacyMixedPC.Low} DCR on {PrivacyMixedPC.Low Date}.

![StakeShuffle Daily Mixed and Unspent Supply (DCR) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Daily_MixedUnspent_DCR.png?raw=true "StakeShuffle Daily Mixed and Unspent Supply (DCR) - Data: dcrdata.org")

In percentage terms over the total DCR circulating supply, throughout the month of {Issue.MonthStr}, the mixed and unspent supply as tracked by dcrdata.org opened at {PrivacyMixedDCR.Open} DCR and closed at {PrivacyMixedDCR.Close} DCR, reaching a high of {PrivacyMixedDCR.High} DCR on {PrivacyMixedDCR.High Date} and a low of {PrivacyMixedDCR.Low} DCR on {PrivacyMixedDCR.Low Date}.

![StakeShuffle Daily Mixed and Unspent Supply (%) - Data: dcrdata.org](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/Stakeshuffle_Daily_MixedUnspent_PC.png?raw=true "StakeShuffle Daily Mixed and Unspent Supply (%) - Data: dcrdata.org")

[Back to Contents](#contents)

## Decentralized Treasury

### Treasury Balance
_The treasury balance represents the sum of DCR across the decentralized treasury account and the legacy treasury._

As of the end of {Issue.Month}, the value of Decred's treasury balance was {treasuryBalanceDCR.Close}. Representing a 

[Back to Contents](#contents)

### Treasury Flows

[Back to Contents](#contents)

## Lightning Network

_The Lightning Network is a decentralized system for instant, high-volume micropayments that removes the risk of delegating custody of funds to trusted third parties._

### Channel Count
_A Lightning channel is a bidirectional payment channel, meaning both parties can send and receive payments across the channel. Lightning channels comprise the Lightning Network and have a defined DCR capacity. This capacity is split between the two parties to the channel, and DCR is moved from one side of the channel to the other by Lightning transactions._

During the month of {Issue.MonthStr}, the daily channel count of Decred's Lightning Network opened at {lnChannels.Open} and closed at {lnChannels.Close}, reaching a high of {lnChannels.High} on {lnChannels.High Date} and a low of {lnChannels.Low} on {lnChannels.Low Date}.

![Decred Lightning Network Channel Count (DCR)](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/DCRLN_Daily_ChannelCount.png?raw=true "Decred Lightning Network Channel Count")

[Back to Contents](#contents)

### Network Capacity
_Lightning capacity is the backbone and liquidity between nodes within the Decred Lightning network. Every new node joining the Decred lightning network must provide liquidity to spend._

During the month of {Issue.MonthStr}, the daily network capacity of Decred's Lightning Network opened at {lnCapacity.Open} DCR and closed at {lnCapacity.Close} DCR, reaching a high of {lnCapacity.High} DCR on {lnCapacity.High Date} and a low of {lnCapacity.Low} DCR on {lnCapacity.Low Date}.

![Decred Lightning Network Capacity (DCR)](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/DCRLN_Daily_Capacity.png?raw=true "Decred Lightning Network Capacity (DCR)")

[Back to Contents](#contents)

### Node Count
_Lightning node is software that connects and interacts with the main Decred network and also within the Decred's Lightning Network itself_

During the month of {Issue.MonthStr}, the daily channel count of Decred's Lightning Network opened at {lnNodes.Open} and closed at {lnNodes.Close}, reaching a high of {lnNodes.High} on {lnNodes.High Date} and a low of {lnNodes.Low} on {lnNodes.Low Date}.

![Decred Lightning Network Node Count (DCR)](https://github.com/bochinchero/dcrsnapshots/blob/main/{Issue.Year}-{Issue.Month}/1920/DCRLN_Daily_NodeCount.png?raw=true "Decred Lightning Network Node Count")

[Back to Contents](#contents)

## Decentralized Exchange

_DCRDEX is a non-custodial, privacy-respecting exchange for trustless trading, powered by atomic swaps._

### Trading Volume

[Back to Contents](#contents)

## Markets & Valuations

###  DCR/USD

[Back to Contents](#contents)

###  DCR/BTC

[Back to Contents](#contents)


