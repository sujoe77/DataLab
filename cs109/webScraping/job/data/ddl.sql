create table public.jobs_old
(
    title    text,
    company  text,
    city     text,
    pub_date text,
    link     text
        constraint jobs_old_unique_link
            unique,
    tags     text,
    add_time timestamp with time zone
);

alter table public.jobs
    owner to postgres;

