/* Write your PL/SQL query statement below */
select p.firstName, p.lastName, a.city, a.state from Person p Left Join Address a on p.personId = a.personId;