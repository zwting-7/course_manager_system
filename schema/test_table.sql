DROP TABLE IF EXISTS student;
CREATE TABLE IF NOT EXISTS student  (
    sn       INTEGER,     --序号
    no       VARCHAR(10), --学号
    name     TEXT,        --姓名
    gender   CHAR(1),     --性别(F/M/O)
    class_sn  INTEGER,    --for class  
    enrolled DATE,        --入学时间
    PRIMARY KEY(sn)
);

CREATE SEQUENCE seq_student_sn 
    START 10000 INCREMENT 1 OWNED BY student.sn;
ALTER TABLE student ALTER sn 
    SET DEFAULT nextval('seq_student_sn');
-- 学号唯一
CREATE UNIQUE INDEX idx_student_no ON student(no);

-- === 课程表
DROP TABLE IF EXISTS course;
CREATE TABLE IF NOT EXISTS course  (
    sn       INTEGER,     --序号
    no       VARCHAR(10), --课程号
    name     TEXT,        --课程名称
    PRIMARY KEY(sn)
);
CREATE SEQUENCE seq_course_sn 
    START 10000 INCREMENT 1 OWNED BY course.sn;
ALTER TABLE course ALTER sn 
    SET DEFAULT nextval('seq_course_sn');
CREATE UNIQUE INDEX idx_course_no ON course(no);

--table for teacher
DROP TABLE IF EXISTS teacher;
CREATE TABLE IF NOT EXISTS teacher  (
    sn       INTEGER,     --序号
    no       VARCHAR(10), --工号
    name     TEXT,        --姓名
    gender   CHAR(1),     --性别(F/M/O)
    PRIMARY KEY(sn)
);
CREATE SEQUENCE seq_teacher_sn 
    START 10000 INCREMENT 1 OWNED BY teacher.sn;
ALTER TABLE teacher ALTER sn 
    SET DEFAULT nextval('seq_teacher_sn');
CREATE UNIQUE INDEX idx_teacher_no ON teacher(no);

DROP TABLE IF EXISTS class;
CREATE TABLE IF NOT EXISTS class (
    sn       INTEGER,     --序号
    no       VARCHAR(10),     --班级ID
    classname     TEXT,   --班级名
    PRIMARY KEY(sn)
);

CREATE SEQUENCE seq_class_sn 
    START 10000 INCREMENT 1 OWNED BY class.sn;
ALTER TABLE class ALTER sn 
    SET DEFAULT nextval('seq_class_sn');
CREATE UNIQUE INDEX idx_class_no ON class(no);

DROP TABLE IF EXISTS class_schedule;
CREATE TABLE IF NOT EXISTS class_schedule  (
    class_sn       INTEGER,     --班级序号
    teacher_sn     INTEGER,     --老师序号
    course_sn      INTEGER,     --课程序号
    weeks          TEXT,
    lessons        INTEGER not null ,
    schedule_year   CHAR(20),      
    remark         CHAR(100),    --remark for the weeks of the courses
    PRIMARY KEY(class_sn,teacher_sn,course_sn,weeks,lessons)
); 


DROP TABLE IF EXISTS course_grade;
CREATE TABLE IF NOT EXISTS course_grade  (
    stu_sn INTEGER,     -- 学生序号
    cou_sn INTEGER,     -- 课程序号
    grade  NUMERIC(5,2), -- 最终成绩
    PRIMARY KEY(stu_sn, cou_sn)
);



ALTER TABLE course_grade 
    ADD CONSTRAINT stu_sn_fk FOREIGN KEY (stu_sn) REFERENCES student(sn);
ALTER TABLE course_grade 
    ADD CONSTRAINT cou_sn_fk FOREIGN KEY (cou_sn) REFERENCES course(sn);



ALTER TABLE student 
    ADD CONSTRAINT stu_class_fk FOREIGN KEY (class_sn) REFERENCES class(sn);
ALTER TABLE class_schedule 
    ADD CONSTRAINT class_sn_fk FOREIGN KEY (class_sn) REFERENCES class(sn);
ALTER TABLE class_schedule 
    ADD CONSTRAINT teacher_sn_fk FOREIGN KEY (teacher_sn) REFERENCES teacher(sn);
ALTER TABLE class_schedule 
    ADD CONSTRAINT course_sn_fk FOREIGN KEY (course_sn) REFERENCES course(sn);