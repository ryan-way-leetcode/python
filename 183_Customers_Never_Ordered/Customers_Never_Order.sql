use customers_who_never_ordered;

select Name as Customers
from Customers c
left join Orders o
on c.Id = o.CustomerId
where o.CustomerId is null;