-- Schema for pomodoro stats db

create table sessions (
    start_time  timestamp not null primary key,
    end_time    timestamp,
    planned     integer,
    done        integer
);

create table pomodoros (
    start_time   timestamp not null primary key,
    end_time     timestamp,
    productivity integer,
    interupted   integer default 0,
    session_id   integer not null references sessions(start_time)
);
