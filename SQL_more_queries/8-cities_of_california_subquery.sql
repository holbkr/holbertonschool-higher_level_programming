-- Script that return all the cities that are from California
SELECT `id`, `name` FROM `cities`
WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = "California");
