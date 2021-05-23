-- What are the top 5 brands by receipts scanned for most recent month?
select brandCode, count(receiptId) as scanTimes from 
(
	select receipts.receiptId as receiptId, brandCode from receiptitemlist
	inner join receipts on receiptitemlist.receiptId = receipts.receiptId
	where receiptitemlist.brandCode is not null
	and receipts.scanDate between '2021-02-01 00:00:00' and '2021-03-01 00:00:00'
)t1
group by brandCode 
order by count(t1.receiptId) desc
limit 5
;

-- How does the ranking of the top 5 brands by receipts scanned for the recent month compare to the ranking for the previous month?
select brandCode, count(receiptId) as scanTimes from 
(
	select receipts.receiptId as receiptId, brandCode from receiptitemlist
	inner join receipts on receiptitemlist.receiptId = receipts.receiptId
	where receiptitemlist.brandCode is not null
	and receipts.scanDate between '2021-01-01 00:00:00' and '2021-02-01 00:00:00'
)t1
group by brandCode 
order by count(t1.receiptId) desc
limit 5
;

-- When considering average spend from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?
select avg(case when rewardsReceiptStatus = 'FINISHED' then totalSpent end) as Accepted_average,
avg(case when rewardsReceiptStatus = 'REJECTED' then totalSpent end) as Rejected_average
from receipts
;

-- When considering total number of items purchased from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?
select avg(case when rewardsReceiptStatus = 'FINISHED' then purchasedItemCount end) as Accepted_average,
avg(case when rewardsReceiptStatus = 'REJECTED' then purchasedItemCount end) as Rejected_average
from receipts
;

-- Which brand has the most spend among users who were created within the past 6 months?
select brandCode, sum(finalPrice) as total_spend from(
	select brandCode, finalPrice from receipts
	inner join receiptitemlist on receipts.receiptId = receiptitemlist.receiptId
	inner join users on receipts.userId = users.userId
	where users.createdDate between current_date() - interval 6 month and current_date() 
	and brandCode is not null
)t1
group by brandCode
order by sum(finalPrice) desc
limit 1
;
-- Which brand has the most transactions among users who were created within the past 6 months?
select brandCode, count(1) as transactions from(
	select brandCode, finalPrice from receipts
	inner join receiptitemlist on receipts.receiptId = receiptitemlist.receiptId
	inner join users on receipts.userId = users.userId
	where users.createdDate between current_date() - interval 6 month and current_date() 
	and brandCode is not null
)t1
group by brandCode
order by count(1) desc
limit 1
;


