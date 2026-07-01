from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register")
def register():
    return {
        "message": "User Registration API Working"
    }


@router.post("/login")
def login():
    return {
        "message": "Login API Working"
    }


@router.put("/update-profile")
def update_profile():
    return {
        "message": "Profile Update API Working"
    }