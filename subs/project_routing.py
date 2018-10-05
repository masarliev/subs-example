from channels import include


project_routing = [
    include("subs.app_routing.app_routing", path=r"^/core"),
]