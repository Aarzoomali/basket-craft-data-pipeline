-- models/staging/stg_website_sessions.sql

WITH raw_sessions AS (
    SELECT
        website_session_id,
        created_at AS website_session_created_at,  -- Rename created_at
        utm_source,                                -- ✅ ADD THIS LINE
        is_repeat_session
    FROM raw.website_sessions
)

SELECT
    website_session_id,
    website_session_created_at,
    utm_source,                                    -- ✅ Ensure it's included
    is_repeat_session,
    CURRENT_TIMESTAMP AS loaded_at                 -- Add loaded_at with the current timestamp
FROM raw_sessions

