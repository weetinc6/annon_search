create table `a_search` (
    `sid` int(30) auto_increment,
    `s_name` text not null,
    `s_descript` text not null,
    `s_favicon` text not null,
    `s_link` text not null,
    primary key(`sid`)
)
engine=myisam character set utf8 collate=utf8_general_ci;