-- models/warehouse/fct_website_sessions_utm_source_daily.sql

with sessions as (
    select * from {{ ref('stg_website_sessions') }}
),

aggregated as (
    select
        date(website_session_created_at) as website_session_day,
        utm_source,
        count(website_session_id) as sessions,
        sum(is_repeat_session)::int as repeat_sessions,
        round(
            (sum(is_repeat_session)::numeric / count(website_session_id)) * 100, 2
        ) as repeat_sessions_pct
    from sessions
    group by 1, 2
)

select * from aggregated
