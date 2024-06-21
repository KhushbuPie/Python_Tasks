-- create_materialized_views.sql
CREATE MATERIALIZED VIEW post_with_details AS
SELECT
    p.id AS post_id,
    p.title,
    p.body,
    p.created_on,
    p.last_modified,
    STRING_AGG(c.name, ', ') AS category_names,
    STRING_AGG(co.author || ': ' || co.body, ', ') AS comment_details
FROM
    blog_post p
LEFT JOIN
    blog_post_categories pc ON p.id = pc.post_id
LEFT JOIN
    blog_category c ON c.id = pc.category_id
LEFT JOIN
    blog_comment co ON p.id = co.post_id
GROUP BY
    p.id;

CREATE INDEX idx_post_with_details_post_id ON post_with_details(post_id);
