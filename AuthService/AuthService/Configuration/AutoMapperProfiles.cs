using AutoMapper;
using AuthService.DTOs;
using AuthService.Entities;

namespace AuthService.Configuration
{
    public class AutoMapperProfiles : Profile {
        public AutoMapperProfiles()
        {
            CreateMap<Stock, StockDto>();
            CreateMap<UpsertStockDto, Stock>();
    }
    }
}
