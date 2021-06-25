 SELECT cs.course_sn, cs.teacher_sn, 
            c.name as cou_name, 
            t.name as teacher_name,
            cs.weeks,
            cs.lessons,
            cs.remark,
            cs.schedule_year 
        FROM class_schedule as cs 
            INNER JOIN teacher as t ON cs.teacher_sn = t.sn
            INNER JOIN course as c  ON cs.course_sn = c.sn
        WHERE schedule_year = '2020春'
SELECT * from class_schedule