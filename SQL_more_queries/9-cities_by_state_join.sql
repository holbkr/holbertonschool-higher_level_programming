-- Script that display several elements from differents table using a join
SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
FROM `cities`
INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`
ORDER BY `cities`.`id` ASC;
