-- models/staging/stg_website_sessions.sql

with source as (
    select * from raw.website_sessions
),

renamed as (
    select
        website_session_id,
        created_at as website_session_created_at,
        user_id,
        is_repeat_session,
        utm_source,
        utm_campaign,
        utm_content,
        device_type,
        http_referer,
        current_timestamp as loaded_at
    from source
)

select * from renamed
