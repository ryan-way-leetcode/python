use delete_duplicate_emails;

delete from 
(select Id, Email, Occurence
from Person
left join 
    (select Email as NOTTHISONE, COUNT(Email) as Occurence
    from Person 
    group by Email) as Occurences
on Person.Email = Occurences.NOTTHISONE
where Occurence > 1) as ToDelete;